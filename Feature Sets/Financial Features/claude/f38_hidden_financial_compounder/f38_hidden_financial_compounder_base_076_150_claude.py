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

# ===== folder domain primitives =====
def _f38_undervalued_proxy(pb, w):
    m = pb.rolling(w, min_periods=max(1, w // 2)).mean()
    return (m - pb) * pb


def _f38_low_attention_growth(volume, eps, w):
    inv_attn = _safe_div(eps, volume.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))
    return inv_attn * volume


def _f38_hidden_compounder_score(pb, roe, w):
    m = pb.rolling(w, min_periods=max(1, w // 2)).mean()
    return (m - pb) * roe * pb

def f38hfc_f38_hidden_financial_compounder_mixuh_21d_base_v076_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 21)
    b = _f38_hidden_compounder_score(pb, roe, 21)
    result = (a + b) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_mixuh_63d_base_v077_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 63)
    b = _f38_hidden_compounder_score(pb, roe, 63)
    result = (a + b) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_mixuh_126d_base_v078_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 126)
    b = _f38_hidden_compounder_score(pb, roe, 126)
    result = (a + b) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_mixuh_252d_base_v079_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 252)
    b = _f38_hidden_compounder_score(pb, roe, 252)
    result = (a + b) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_mixul_21d_base_v080_signal(pb, volume, eps, closeadj):
    a = _f38_undervalued_proxy(pb, 21)
    b = _f38_low_attention_growth(volume, eps, 21)
    result = a * np.sign(b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_mixul_63d_base_v081_signal(pb, volume, eps, closeadj):
    a = _f38_undervalued_proxy(pb, 63)
    b = _f38_low_attention_growth(volume, eps, 63)
    result = a * np.sign(b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_mixul_126d_base_v082_signal(pb, volume, eps, closeadj):
    a = _f38_undervalued_proxy(pb, 126)
    b = _f38_low_attention_growth(volume, eps, 126)
    result = a * np.sign(b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_mixul_252d_base_v083_signal(pb, volume, eps, closeadj):
    a = _f38_undervalued_proxy(pb, 252)
    b = _f38_low_attention_growth(volume, eps, 252)
    result = a * np.sign(b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervanom_21d_base_v084_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = (base - _mean(base, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervanom_63d_base_v085_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = (base - _mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervanom_126d_base_v086_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervanom_252d_base_v087_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 252)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidanom_21d_base_v088_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = (base - _mean(base, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidanom_63d_base_v089_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 63)
    result = (base - _mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidanom_126d_base_v090_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 126)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidanom_252d_base_v091_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 252)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loanom_21d_base_v092_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 21)
    result = (base - _mean(base, 42)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loanom_63d_base_v093_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 63)
    result = (base - _mean(base, 126)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loanom_126d_base_v094_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 126)
    result = (base - _mean(base, 252)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loanom_252d_base_v095_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 252)
    result = (base - _mean(base, 504)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervsqrt_21d_base_v096_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = base * np.sqrt(21) / np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervsqrt_63d_base_v097_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = base * np.sqrt(63) / np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervsqrt_126d_base_v098_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = base * np.sqrt(126) / np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervsqrt_252d_base_v099_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 252)
    result = base * np.sqrt(252) / np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidsqrt_21d_base_v100_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = base * np.sqrt(21) / np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidsqrt_63d_base_v101_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 63)
    result = base * np.sqrt(63) / np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidsqrt_126d_base_v102_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 126)
    result = base * np.sqrt(126) / np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidsqrt_252d_base_v103_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 252)
    result = base * np.sqrt(252) / np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_losqrt_21d_base_v104_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 21)
    result = base * np.sqrt(21) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_losqrt_63d_base_v105_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 63)
    result = base * np.sqrt(63) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_losqrt_126d_base_v106_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 126)
    result = base * np.sqrt(126) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_losqrt_252d_base_v107_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 252)
    result = base * np.sqrt(252) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervlog_21d_base_v108_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervlog_63d_base_v109_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervlog_126d_base_v110_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervlog_252d_base_v111_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidlog_21d_base_v112_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidlog_63d_base_v113_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidlog_126d_base_v114_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidlog_252d_base_v115_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhweighted_21d_base_v116_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 21)
    b = _f38_hidden_compounder_score(pb, roe, 21)
    result = (0.3 * a + 0.7 * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhweighted_63d_base_v117_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 63)
    b = _f38_hidden_compounder_score(pb, roe, 63)
    result = (0.3 * a + 0.7 * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhweighted_126d_base_v118_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 126)
    b = _f38_hidden_compounder_score(pb, roe, 126)
    result = (0.3 * a + 0.7 * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhweighted_252d_base_v119_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 252)
    b = _f38_hidden_compounder_score(pb, roe, 252)
    result = (0.3 * a + 0.7 * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhweightedr_21d_base_v120_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 21)
    b = _f38_hidden_compounder_score(pb, roe, 21)
    result = (0.7 * a + 0.3 * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhweightedr_63d_base_v121_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 63)
    b = _f38_hidden_compounder_score(pb, roe, 63)
    result = (0.7 * a + 0.3 * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhweightedr_126d_base_v122_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 126)
    b = _f38_hidden_compounder_score(pb, roe, 126)
    result = (0.7 * a + 0.3 * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhweightedr_252d_base_v123_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 252)
    b = _f38_hidden_compounder_score(pb, roe, 252)
    result = (0.7 * a + 0.3 * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervdiff_21d_base_v124_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervdiff_63d_base_v125_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervdiff_126d_base_v126_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = (base - base.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervdiff_252d_base_v127_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hiddiff_21d_base_v128_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hiddiff_63d_base_v129_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hiddiff_126d_base_v130_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 126)
    result = (base - base.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hiddiff_252d_base_v131_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_lodiff_21d_base_v132_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 21)
    result = (base - base.shift(21)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_lodiff_63d_base_v133_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 63)
    result = (base - base.shift(63)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_lodiff_126d_base_v134_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 126)
    result = (base - base.shift(126)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_lodiff_252d_base_v135_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 252)
    result = (base - base.shift(252)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervstdl_21d_base_v136_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervstdl_63d_base_v137_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervstdl_126d_base_v138_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidstdB_21d_base_v139_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = _std(base, 21) * closeadj * np.log1p(_mean(closeadj, 5).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidstdB_63d_base_v140_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 63)
    result = _std(base, 63) * closeadj * np.log1p(_mean(closeadj, 10).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidstdB_126d_base_v141_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 126)
    result = _std(base, 126) * closeadj * np.log1p(_mean(closeadj, 42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhsqA_21d_base_v142_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 21)
    b = _f38_hidden_compounder_score(pb, roe, 21)
    result = (a - b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhsqA_63d_base_v143_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 63)
    b = _f38_hidden_compounder_score(pb, roe, 63)
    result = (a - b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhsqA_126d_base_v144_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 126)
    b = _f38_hidden_compounder_score(pb, roe, 126)
    result = (a - b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_uhsqA_252d_base_v145_signal(pb, roe, closeadj):
    a = _f38_undervalued_proxy(pb, 252)
    b = _f38_hidden_compounder_score(pb, roe, 252)
    result = (a - b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxroe_21d_base_v146_signal(pb, roe, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = base * roe * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxroe_63d_base_v147_signal(pb, roe, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = base * roe * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxroe_126d_base_v148_signal(pb, roe, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = base * roe * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxroe_252d_base_v149_signal(pb, roe, closeadj):
    base = _f38_undervalued_proxy(pb, 252)
    result = base * roe * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidxpb_21d_base_v150_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = base * pb * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38hfc_f38_hidden_financial_compounder_mixuh_21d_base_v076_signal,
    f38hfc_f38_hidden_financial_compounder_mixuh_63d_base_v077_signal,
    f38hfc_f38_hidden_financial_compounder_mixuh_126d_base_v078_signal,
    f38hfc_f38_hidden_financial_compounder_mixuh_252d_base_v079_signal,
    f38hfc_f38_hidden_financial_compounder_mixul_21d_base_v080_signal,
    f38hfc_f38_hidden_financial_compounder_mixul_63d_base_v081_signal,
    f38hfc_f38_hidden_financial_compounder_mixul_126d_base_v082_signal,
    f38hfc_f38_hidden_financial_compounder_mixul_252d_base_v083_signal,
    f38hfc_f38_hidden_financial_compounder_undervanom_21d_base_v084_signal,
    f38hfc_f38_hidden_financial_compounder_undervanom_63d_base_v085_signal,
    f38hfc_f38_hidden_financial_compounder_undervanom_126d_base_v086_signal,
    f38hfc_f38_hidden_financial_compounder_undervanom_252d_base_v087_signal,
    f38hfc_f38_hidden_financial_compounder_hidanom_21d_base_v088_signal,
    f38hfc_f38_hidden_financial_compounder_hidanom_63d_base_v089_signal,
    f38hfc_f38_hidden_financial_compounder_hidanom_126d_base_v090_signal,
    f38hfc_f38_hidden_financial_compounder_hidanom_252d_base_v091_signal,
    f38hfc_f38_hidden_financial_compounder_loanom_21d_base_v092_signal,
    f38hfc_f38_hidden_financial_compounder_loanom_63d_base_v093_signal,
    f38hfc_f38_hidden_financial_compounder_loanom_126d_base_v094_signal,
    f38hfc_f38_hidden_financial_compounder_loanom_252d_base_v095_signal,
    f38hfc_f38_hidden_financial_compounder_undervsqrt_21d_base_v096_signal,
    f38hfc_f38_hidden_financial_compounder_undervsqrt_63d_base_v097_signal,
    f38hfc_f38_hidden_financial_compounder_undervsqrt_126d_base_v098_signal,
    f38hfc_f38_hidden_financial_compounder_undervsqrt_252d_base_v099_signal,
    f38hfc_f38_hidden_financial_compounder_hidsqrt_21d_base_v100_signal,
    f38hfc_f38_hidden_financial_compounder_hidsqrt_63d_base_v101_signal,
    f38hfc_f38_hidden_financial_compounder_hidsqrt_126d_base_v102_signal,
    f38hfc_f38_hidden_financial_compounder_hidsqrt_252d_base_v103_signal,
    f38hfc_f38_hidden_financial_compounder_losqrt_21d_base_v104_signal,
    f38hfc_f38_hidden_financial_compounder_losqrt_63d_base_v105_signal,
    f38hfc_f38_hidden_financial_compounder_losqrt_126d_base_v106_signal,
    f38hfc_f38_hidden_financial_compounder_losqrt_252d_base_v107_signal,
    f38hfc_f38_hidden_financial_compounder_undervlog_21d_base_v108_signal,
    f38hfc_f38_hidden_financial_compounder_undervlog_63d_base_v109_signal,
    f38hfc_f38_hidden_financial_compounder_undervlog_126d_base_v110_signal,
    f38hfc_f38_hidden_financial_compounder_undervlog_252d_base_v111_signal,
    f38hfc_f38_hidden_financial_compounder_hidlog_21d_base_v112_signal,
    f38hfc_f38_hidden_financial_compounder_hidlog_63d_base_v113_signal,
    f38hfc_f38_hidden_financial_compounder_hidlog_126d_base_v114_signal,
    f38hfc_f38_hidden_financial_compounder_hidlog_252d_base_v115_signal,
    f38hfc_f38_hidden_financial_compounder_uhweighted_21d_base_v116_signal,
    f38hfc_f38_hidden_financial_compounder_uhweighted_63d_base_v117_signal,
    f38hfc_f38_hidden_financial_compounder_uhweighted_126d_base_v118_signal,
    f38hfc_f38_hidden_financial_compounder_uhweighted_252d_base_v119_signal,
    f38hfc_f38_hidden_financial_compounder_uhweightedr_21d_base_v120_signal,
    f38hfc_f38_hidden_financial_compounder_uhweightedr_63d_base_v121_signal,
    f38hfc_f38_hidden_financial_compounder_uhweightedr_126d_base_v122_signal,
    f38hfc_f38_hidden_financial_compounder_uhweightedr_252d_base_v123_signal,
    f38hfc_f38_hidden_financial_compounder_undervdiff_21d_base_v124_signal,
    f38hfc_f38_hidden_financial_compounder_undervdiff_63d_base_v125_signal,
    f38hfc_f38_hidden_financial_compounder_undervdiff_126d_base_v126_signal,
    f38hfc_f38_hidden_financial_compounder_undervdiff_252d_base_v127_signal,
    f38hfc_f38_hidden_financial_compounder_hiddiff_21d_base_v128_signal,
    f38hfc_f38_hidden_financial_compounder_hiddiff_63d_base_v129_signal,
    f38hfc_f38_hidden_financial_compounder_hiddiff_126d_base_v130_signal,
    f38hfc_f38_hidden_financial_compounder_hiddiff_252d_base_v131_signal,
    f38hfc_f38_hidden_financial_compounder_lodiff_21d_base_v132_signal,
    f38hfc_f38_hidden_financial_compounder_lodiff_63d_base_v133_signal,
    f38hfc_f38_hidden_financial_compounder_lodiff_126d_base_v134_signal,
    f38hfc_f38_hidden_financial_compounder_lodiff_252d_base_v135_signal,
    f38hfc_f38_hidden_financial_compounder_undervstdl_21d_base_v136_signal,
    f38hfc_f38_hidden_financial_compounder_undervstdl_63d_base_v137_signal,
    f38hfc_f38_hidden_financial_compounder_undervstdl_126d_base_v138_signal,
    f38hfc_f38_hidden_financial_compounder_hidstdB_21d_base_v139_signal,
    f38hfc_f38_hidden_financial_compounder_hidstdB_63d_base_v140_signal,
    f38hfc_f38_hidden_financial_compounder_hidstdB_126d_base_v141_signal,
    f38hfc_f38_hidden_financial_compounder_uhsqA_21d_base_v142_signal,
    f38hfc_f38_hidden_financial_compounder_uhsqA_63d_base_v143_signal,
    f38hfc_f38_hidden_financial_compounder_uhsqA_126d_base_v144_signal,
    f38hfc_f38_hidden_financial_compounder_uhsqA_252d_base_v145_signal,
    f38hfc_f38_hidden_financial_compounder_undervxroe_21d_base_v146_signal,
    f38hfc_f38_hidden_financial_compounder_undervxroe_63d_base_v147_signal,
    f38hfc_f38_hidden_financial_compounder_undervxroe_126d_base_v148_signal,
    f38hfc_f38_hidden_financial_compounder_undervxroe_252d_base_v149_signal,
    f38hfc_f38_hidden_financial_compounder_hidxpb_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_HIDDEN_FINANCIAL_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f38_undervalued_proxy", "_f38_low_attention_growth", "_f38_hidden_compounder_score")
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
    print(f"OK f38_hidden_financial_compounder_base_076_150_claude: {n_features} features pass")
