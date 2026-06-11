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

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_rawx_10d_base_v076_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_mean42d_base_v077_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_std189d_base_v078_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_z378d_base_v079_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_rank252d_base_v080_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_abs10d_base_v081_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_sq42d_base_v082_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_max189d_base_v083_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_min378d_base_v084_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_rng252d_base_v085_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_med10d_base_v086_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_q7542d_base_v087_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_q25189d_base_v088_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_ema378d_base_v089_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_emastd252d_base_v090_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_diff10d_base_v091_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_pct42d_base_v092_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_log189d_base_v093_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_sign378d_base_v094_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_sum252d_base_v095_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_zsq10d_base_v096_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_centered42d_base_v097_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_ratio189d_base_v098_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_skew378d_base_v099_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfgalt_kurt252d_base_v100_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_rawx_10d_base_v101_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_mean42d_base_v102_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_std189d_base_v103_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_z378d_base_v104_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_rank252d_base_v105_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_abs10d_base_v106_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_sq42d_base_v107_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_max189d_base_v108_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_min378d_base_v109_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_rng252d_base_v110_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_med10d_base_v111_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_q7542d_base_v112_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_q25189d_base_v113_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_ema378d_base_v114_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_emastd252d_base_v115_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_diff10d_base_v116_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_pct42d_base_v117_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_log189d_base_v118_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_sign378d_base_v119_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_sum252d_base_v120_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_zsq10d_base_v121_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_centered42d_base_v122_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_ratio189d_base_v123_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_skew378d_base_v124_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attnalt_kurt252d_base_v125_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_rawx_10d_base_v126_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_mean42d_base_v127_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_std189d_base_v128_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_z378d_base_v129_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_rank252d_base_v130_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_abs10d_base_v131_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_sq42d_base_v132_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_max189d_base_v133_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_min378d_base_v134_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_rng252d_base_v135_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_med10d_base_v136_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_q7542d_base_v137_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_q25189d_base_v138_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_ema378d_base_v139_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_emastd252d_base_v140_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_diff10d_base_v141_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_pct42d_base_v142_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_log189d_base_v143_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_sign378d_base_v144_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_sum252d_base_v145_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_zsq10d_base_v146_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_centered42d_base_v147_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_ratio189d_base_v148_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_skew378d_base_v149_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcsalt_kurt252d_base_v150_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_rawx_10d_base_v076_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_mean42d_base_v077_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_std189d_base_v078_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_z378d_base_v079_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_rank252d_base_v080_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_abs10d_base_v081_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_sq42d_base_v082_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_max189d_base_v083_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_min378d_base_v084_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_rng252d_base_v085_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_med10d_base_v086_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_q7542d_base_v087_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_q25189d_base_v088_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_ema378d_base_v089_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_emastd252d_base_v090_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_diff10d_base_v091_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_pct42d_base_v092_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_log189d_base_v093_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_sign378d_base_v094_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_sum252d_base_v095_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_zsq10d_base_v096_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_centered42d_base_v097_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_ratio189d_base_v098_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_skew378d_base_v099_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfgalt_kurt252d_base_v100_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_rawx_10d_base_v101_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_mean42d_base_v102_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_std189d_base_v103_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_z378d_base_v104_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_rank252d_base_v105_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_abs10d_base_v106_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_sq42d_base_v107_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_max189d_base_v108_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_min378d_base_v109_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_rng252d_base_v110_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_med10d_base_v111_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_q7542d_base_v112_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_q25189d_base_v113_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_ema378d_base_v114_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_emastd252d_base_v115_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_diff10d_base_v116_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_pct42d_base_v117_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_log189d_base_v118_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_sign378d_base_v119_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_sum252d_base_v120_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_zsq10d_base_v121_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_centered42d_base_v122_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_ratio189d_base_v123_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_skew378d_base_v124_signal,
    f29hbc_f29_hidden_brand_compounder_attnalt_kurt252d_base_v125_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_rawx_10d_base_v126_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_mean42d_base_v127_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_std189d_base_v128_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_z378d_base_v129_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_rank252d_base_v130_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_abs10d_base_v131_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_sq42d_base_v132_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_max189d_base_v133_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_min378d_base_v134_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_rng252d_base_v135_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_med10d_base_v136_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_q7542d_base_v137_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_q25189d_base_v138_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_ema378d_base_v139_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_emastd252d_base_v140_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_diff10d_base_v141_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_pct42d_base_v142_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_log189d_base_v143_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_sign378d_base_v144_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_sum252d_base_v145_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_zsq10d_base_v146_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_centered42d_base_v147_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_ratio189d_base_v148_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_skew378d_base_v149_signal,
    f29hbc_f29_hidden_brand_compounder_hcsalt_kurt252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_HIDDEN_BRAND_COMPOUNDER_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f29_hidden_brand_compounder_base_076_150_claude: {n_features} features pass")
