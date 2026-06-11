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

def f29hbc_f29_hidden_brand_compounder_qfcfg_rawx_21d_base_v001_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_mean63d_base_v002_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_std126d_base_v003_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_z252d_base_v004_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_rank504d_base_v005_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_abs21d_base_v006_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_sq63d_base_v007_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_max126d_base_v008_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_min252d_base_v009_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_rng504d_base_v010_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_med21d_base_v011_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_q7563d_base_v012_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_q25126d_base_v013_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_ema252d_base_v014_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_emastd504d_base_v015_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_diff21d_base_v016_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_pct63d_base_v017_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_log126d_base_v018_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_sign252d_base_v019_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_sum504d_base_v020_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_zsq21d_base_v021_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_centered63d_base_v022_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_ratio126d_base_v023_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_skew252d_base_v024_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_kurt504d_base_v025_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_rawx_21d_base_v026_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_mean63d_base_v027_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_std126d_base_v028_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_z252d_base_v029_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_rank504d_base_v030_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_abs21d_base_v031_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_sq63d_base_v032_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_max126d_base_v033_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_min252d_base_v034_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_rng504d_base_v035_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_med21d_base_v036_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_q7563d_base_v037_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_q25126d_base_v038_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_ema252d_base_v039_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_emastd504d_base_v040_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_diff21d_base_v041_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_pct63d_base_v042_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_log126d_base_v043_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_sign252d_base_v044_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_sum504d_base_v045_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_zsq21d_base_v046_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_centered63d_base_v047_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_ratio126d_base_v048_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_skew252d_base_v049_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_kurt504d_base_v050_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_rawx_21d_base_v051_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_mean63d_base_v052_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_std126d_base_v053_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_z252d_base_v054_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_rank504d_base_v055_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_abs21d_base_v056_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_sq63d_base_v057_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_max126d_base_v058_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_min252d_base_v059_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_rng504d_base_v060_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_med21d_base_v061_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_q7563d_base_v062_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_q25126d_base_v063_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_ema252d_base_v064_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_emastd504d_base_v065_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_diff21d_base_v066_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_pct63d_base_v067_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_log126d_base_v068_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_sign252d_base_v069_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_sum504d_base_v070_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_zsq21d_base_v071_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_centered63d_base_v072_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_ratio126d_base_v073_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_skew252d_base_v074_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_kurt504d_base_v075_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29hbc_f29_hidden_brand_compounder_qfcfg_rawx_21d_base_v001_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_mean63d_base_v002_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_std126d_base_v003_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_z252d_base_v004_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_rank504d_base_v005_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_abs21d_base_v006_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_sq63d_base_v007_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_max126d_base_v008_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_min252d_base_v009_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_rng504d_base_v010_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_med21d_base_v011_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_q7563d_base_v012_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_q25126d_base_v013_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_ema252d_base_v014_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_emastd504d_base_v015_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_diff21d_base_v016_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_pct63d_base_v017_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_log126d_base_v018_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_sign252d_base_v019_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_sum504d_base_v020_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_zsq21d_base_v021_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_centered63d_base_v022_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_ratio126d_base_v023_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_skew252d_base_v024_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_kurt504d_base_v025_signal,
    f29hbc_f29_hidden_brand_compounder_attn_rawx_21d_base_v026_signal,
    f29hbc_f29_hidden_brand_compounder_attn_mean63d_base_v027_signal,
    f29hbc_f29_hidden_brand_compounder_attn_std126d_base_v028_signal,
    f29hbc_f29_hidden_brand_compounder_attn_z252d_base_v029_signal,
    f29hbc_f29_hidden_brand_compounder_attn_rank504d_base_v030_signal,
    f29hbc_f29_hidden_brand_compounder_attn_abs21d_base_v031_signal,
    f29hbc_f29_hidden_brand_compounder_attn_sq63d_base_v032_signal,
    f29hbc_f29_hidden_brand_compounder_attn_max126d_base_v033_signal,
    f29hbc_f29_hidden_brand_compounder_attn_min252d_base_v034_signal,
    f29hbc_f29_hidden_brand_compounder_attn_rng504d_base_v035_signal,
    f29hbc_f29_hidden_brand_compounder_attn_med21d_base_v036_signal,
    f29hbc_f29_hidden_brand_compounder_attn_q7563d_base_v037_signal,
    f29hbc_f29_hidden_brand_compounder_attn_q25126d_base_v038_signal,
    f29hbc_f29_hidden_brand_compounder_attn_ema252d_base_v039_signal,
    f29hbc_f29_hidden_brand_compounder_attn_emastd504d_base_v040_signal,
    f29hbc_f29_hidden_brand_compounder_attn_diff21d_base_v041_signal,
    f29hbc_f29_hidden_brand_compounder_attn_pct63d_base_v042_signal,
    f29hbc_f29_hidden_brand_compounder_attn_log126d_base_v043_signal,
    f29hbc_f29_hidden_brand_compounder_attn_sign252d_base_v044_signal,
    f29hbc_f29_hidden_brand_compounder_attn_sum504d_base_v045_signal,
    f29hbc_f29_hidden_brand_compounder_attn_zsq21d_base_v046_signal,
    f29hbc_f29_hidden_brand_compounder_attn_centered63d_base_v047_signal,
    f29hbc_f29_hidden_brand_compounder_attn_ratio126d_base_v048_signal,
    f29hbc_f29_hidden_brand_compounder_attn_skew252d_base_v049_signal,
    f29hbc_f29_hidden_brand_compounder_attn_kurt504d_base_v050_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_rawx_21d_base_v051_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_mean63d_base_v052_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_std126d_base_v053_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_z252d_base_v054_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_rank504d_base_v055_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_abs21d_base_v056_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_sq63d_base_v057_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_max126d_base_v058_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_min252d_base_v059_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_rng504d_base_v060_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_med21d_base_v061_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_q7563d_base_v062_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_q25126d_base_v063_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_ema252d_base_v064_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_emastd504d_base_v065_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_diff21d_base_v066_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_pct63d_base_v067_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_log126d_base_v068_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_sign252d_base_v069_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_sum504d_base_v070_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_zsq21d_base_v071_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_centered63d_base_v072_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_ratio126d_base_v073_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_skew252d_base_v074_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_kurt504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_HIDDEN_BRAND_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f29_hidden_brand_compounder_base_001_075_claude: {n_features} features pass")
