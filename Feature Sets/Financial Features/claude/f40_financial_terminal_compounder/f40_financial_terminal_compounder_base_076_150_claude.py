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
def _f40_quality_composite(roe, bvps, w):
    rm = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    bg = bvps.pct_change(periods=w)
    return rm * bg * bvps


def _f40_terminal_score(roe, equity, w):
    rm = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    eg = equity.pct_change(periods=w)
    return rm * eg * equity


def _f40_terminal_quality(roe, bvps, closeadj, w):
    rets = closeadj.pct_change()
    vol = rets.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    rm = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    bg = bvps.pct_change(periods=w)
    return rm * bg * closeadj / vol

def f40ftc_f40_financial_terminal_compounder_qtmix_21d_base_v076_signal(roe, bvps, equity, closeadj):
    a = _f40_quality_composite(roe, bvps, 21)
    b = _f40_terminal_score(roe, equity, 21)
    result = (a + b) * closeadj / _mean(closeadj, 21) / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qtmix_63d_base_v077_signal(roe, bvps, equity, closeadj):
    a = _f40_quality_composite(roe, bvps, 63)
    b = _f40_terminal_score(roe, equity, 63)
    result = (a + b) * closeadj / _mean(closeadj, 21) / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qtmix_126d_base_v078_signal(roe, bvps, equity, closeadj):
    a = _f40_quality_composite(roe, bvps, 126)
    b = _f40_terminal_score(roe, equity, 126)
    result = (a + b) * closeadj / _mean(closeadj, 21) / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qtmix_252d_base_v079_signal(roe, bvps, equity, closeadj):
    a = _f40_quality_composite(roe, bvps, 252)
    b = _f40_terminal_score(roe, equity, 252)
    result = (a + b) * closeadj / _mean(closeadj, 21) / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qtqmix_21d_base_v080_signal(roe, bvps, closeadj):
    a = _f40_quality_composite(roe, bvps, 21)
    b = _f40_terminal_quality(roe, bvps, closeadj, 21)
    result = a * np.sign(b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qtqmix_63d_base_v081_signal(roe, bvps, closeadj):
    a = _f40_quality_composite(roe, bvps, 63)
    b = _f40_terminal_quality(roe, bvps, closeadj, 63)
    result = a * np.sign(b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qtqmix_126d_base_v082_signal(roe, bvps, closeadj):
    a = _f40_quality_composite(roe, bvps, 126)
    b = _f40_terminal_quality(roe, bvps, closeadj, 126)
    result = a * np.sign(b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qtqmix_252d_base_v083_signal(roe, bvps, closeadj):
    a = _f40_quality_composite(roe, bvps, 252)
    b = _f40_terminal_quality(roe, bvps, closeadj, 252)
    result = a * np.sign(b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tstqmix_21d_base_v084_signal(roe, bvps, equity, closeadj):
    a = _f40_terminal_score(roe, equity, 21)
    b = _f40_terminal_quality(roe, bvps, closeadj, 21)
    result = (0.5 * a + 0.5 * b) * closeadj / _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tstqmix_63d_base_v085_signal(roe, bvps, equity, closeadj):
    a = _f40_terminal_score(roe, equity, 63)
    b = _f40_terminal_quality(roe, bvps, closeadj, 63)
    result = (0.5 * a + 0.5 * b) * closeadj / _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tstqmix_126d_base_v086_signal(roe, bvps, equity, closeadj):
    a = _f40_terminal_score(roe, equity, 126)
    b = _f40_terminal_quality(roe, bvps, closeadj, 126)
    result = (0.5 * a + 0.5 * b) * closeadj / _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tstqmix_252d_base_v087_signal(roe, bvps, equity, closeadj):
    a = _f40_terminal_score(roe, equity, 252)
    b = _f40_terminal_quality(roe, bvps, closeadj, 252)
    result = (0.5 * a + 0.5 * b) * closeadj / _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcanom_21d_base_v088_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 21)
    result = (base - _mean(base, 42)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcanom_63d_base_v089_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 63)
    result = (base - _mean(base, 126)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcanom_126d_base_v090_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 126)
    result = (base - _mean(base, 252)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcanom_252d_base_v091_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 252)
    result = (base - _mean(base, 504)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tsanom_21d_base_v092_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 21)
    result = (base - _mean(base, 42)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tsanom_63d_base_v093_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 63)
    result = (base - _mean(base, 126)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tsanom_126d_base_v094_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 126)
    result = (base - _mean(base, 252)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tsanom_252d_base_v095_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 252)
    result = (base - _mean(base, 504)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqanom_21d_base_v096_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 21)
    result = (base - _mean(base, 42))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqanom_63d_base_v097_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 63)
    result = (base - _mean(base, 126))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqanom_126d_base_v098_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 126)
    result = (base - _mean(base, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqanom_252d_base_v099_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 252)
    result = (base - _mean(base, 504))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcsqrt_21d_base_v100_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 21)
    result = base * np.sqrt(21) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcsqrt_63d_base_v101_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 63)
    result = base * np.sqrt(63) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcsqrt_126d_base_v102_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 126)
    result = base * np.sqrt(126) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcsqrt_252d_base_v103_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 252)
    result = base * np.sqrt(252) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tssqrt_21d_base_v104_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 21)
    result = base * np.sqrt(21) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tssqrt_63d_base_v105_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 63)
    result = base * np.sqrt(63) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tssqrt_126d_base_v106_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 126)
    result = base * np.sqrt(126) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tssqrt_252d_base_v107_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 252)
    result = base * np.sqrt(252) / np.sqrt(252.0) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqsqrt_21d_base_v108_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 21)
    result = base * np.sqrt(21) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqsqrt_63d_base_v109_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 63)
    result = base * np.sqrt(63) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqsqrt_126d_base_v110_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 126)
    result = base * np.sqrt(126) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqsqrt_252d_base_v111_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 252)
    result = base * np.sqrt(252) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qclog_21d_base_v112_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qclog_63d_base_v113_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qclog_126d_base_v114_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qclog_252d_base_v115_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tslog_21d_base_v116_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tslog_63d_base_v117_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tslog_126d_base_v118_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tslog_252d_base_v119_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqlog_21d_base_v120_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqlog_63d_base_v121_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqlog_126d_base_v122_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqlog_252d_base_v123_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcdiff_21d_base_v124_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 21)
    result = (base - base.shift(21)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcdiff_63d_base_v125_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 63)
    result = (base - base.shift(63)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcdiff_126d_base_v126_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 126)
    result = (base - base.shift(126)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tsdiff_21d_base_v127_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 21)
    result = (base - base.shift(21)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tsdiff_63d_base_v128_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 63)
    result = (base - base.shift(63)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tsdiff_126d_base_v129_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 126)
    result = (base - base.shift(126)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqdiff_21d_base_v130_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 21)
    result = (base - base.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqdiff_63d_base_v131_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 63)
    result = (base - base.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqdiff_126d_base_v132_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 126)
    result = (base - base.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcwt_21d_base_v133_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 21)
    wt = closeadj / _mean(closeadj, 42)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcwt_63d_base_v134_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 63)
    wt = closeadj / _mean(closeadj, 126)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcwt_126d_base_v135_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 126)
    wt = closeadj / _mean(closeadj, 252)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcwt_252d_base_v136_signal(roe, bvps, closeadj):
    base = _f40_quality_composite(roe, bvps, 252)
    wt = closeadj / _mean(closeadj, 504)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tswt_21d_base_v137_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 21)
    wt = closeadj / _mean(closeadj, 42)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tswt_63d_base_v138_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 63)
    wt = closeadj / _mean(closeadj, 126)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tswt_126d_base_v139_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 126)
    wt = closeadj / _mean(closeadj, 252)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tswt_252d_base_v140_signal(roe, equity, closeadj):
    base = _f40_terminal_score(roe, equity, 252)
    wt = closeadj / _mean(closeadj, 504)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqwt_21d_base_v141_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 21)
    wt = closeadj / _mean(closeadj, 42)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqwt_63d_base_v142_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 63)
    wt = closeadj / _mean(closeadj, 126)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqwt_126d_base_v143_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 126)
    wt = closeadj / _mean(closeadj, 252)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqwt_252d_base_v144_signal(roe, bvps, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 252)
    wt = closeadj / _mean(closeadj, 504)
    result = base * wt
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcxeqb_21d_base_v145_signal(roe, bvps, equity, closeadj):
    base = _f40_quality_composite(roe, bvps, 21)
    result = base * _safe_div(equity, _mean(equity, 42)) * closeadj / _mean(closeadj, 21) * np.log1p(_mean(closeadj, 14).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_qcxeqb_63d_base_v146_signal(roe, bvps, equity, closeadj):
    base = _f40_quality_composite(roe, bvps, 63)
    result = base * _safe_div(equity, _mean(equity, 126)) * closeadj / _mean(closeadj, 21) * np.log1p(_mean(closeadj, 42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqxeq_21d_base_v147_signal(roe, bvps, equity, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 21)
    result = base * _safe_div(equity, _mean(equity, 42))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqxeq_63d_base_v148_signal(roe, bvps, equity, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 63)
    result = base * _safe_div(equity, _mean(equity, 126))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqxeq_126d_base_v149_signal(roe, bvps, equity, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 126)
    result = base * _safe_div(equity, _mean(equity, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f40ftc_f40_financial_terminal_compounder_tqxeq_252d_base_v150_signal(roe, bvps, equity, closeadj):
    base = _f40_terminal_quality(roe, bvps, closeadj, 252)
    result = base * _safe_div(equity, _mean(equity, 504))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40ftc_f40_financial_terminal_compounder_qtmix_21d_base_v076_signal,
    f40ftc_f40_financial_terminal_compounder_qtmix_63d_base_v077_signal,
    f40ftc_f40_financial_terminal_compounder_qtmix_126d_base_v078_signal,
    f40ftc_f40_financial_terminal_compounder_qtmix_252d_base_v079_signal,
    f40ftc_f40_financial_terminal_compounder_qtqmix_21d_base_v080_signal,
    f40ftc_f40_financial_terminal_compounder_qtqmix_63d_base_v081_signal,
    f40ftc_f40_financial_terminal_compounder_qtqmix_126d_base_v082_signal,
    f40ftc_f40_financial_terminal_compounder_qtqmix_252d_base_v083_signal,
    f40ftc_f40_financial_terminal_compounder_tstqmix_21d_base_v084_signal,
    f40ftc_f40_financial_terminal_compounder_tstqmix_63d_base_v085_signal,
    f40ftc_f40_financial_terminal_compounder_tstqmix_126d_base_v086_signal,
    f40ftc_f40_financial_terminal_compounder_tstqmix_252d_base_v087_signal,
    f40ftc_f40_financial_terminal_compounder_qcanom_21d_base_v088_signal,
    f40ftc_f40_financial_terminal_compounder_qcanom_63d_base_v089_signal,
    f40ftc_f40_financial_terminal_compounder_qcanom_126d_base_v090_signal,
    f40ftc_f40_financial_terminal_compounder_qcanom_252d_base_v091_signal,
    f40ftc_f40_financial_terminal_compounder_tsanom_21d_base_v092_signal,
    f40ftc_f40_financial_terminal_compounder_tsanom_63d_base_v093_signal,
    f40ftc_f40_financial_terminal_compounder_tsanom_126d_base_v094_signal,
    f40ftc_f40_financial_terminal_compounder_tsanom_252d_base_v095_signal,
    f40ftc_f40_financial_terminal_compounder_tqanom_21d_base_v096_signal,
    f40ftc_f40_financial_terminal_compounder_tqanom_63d_base_v097_signal,
    f40ftc_f40_financial_terminal_compounder_tqanom_126d_base_v098_signal,
    f40ftc_f40_financial_terminal_compounder_tqanom_252d_base_v099_signal,
    f40ftc_f40_financial_terminal_compounder_qcsqrt_21d_base_v100_signal,
    f40ftc_f40_financial_terminal_compounder_qcsqrt_63d_base_v101_signal,
    f40ftc_f40_financial_terminal_compounder_qcsqrt_126d_base_v102_signal,
    f40ftc_f40_financial_terminal_compounder_qcsqrt_252d_base_v103_signal,
    f40ftc_f40_financial_terminal_compounder_tssqrt_21d_base_v104_signal,
    f40ftc_f40_financial_terminal_compounder_tssqrt_63d_base_v105_signal,
    f40ftc_f40_financial_terminal_compounder_tssqrt_126d_base_v106_signal,
    f40ftc_f40_financial_terminal_compounder_tssqrt_252d_base_v107_signal,
    f40ftc_f40_financial_terminal_compounder_tqsqrt_21d_base_v108_signal,
    f40ftc_f40_financial_terminal_compounder_tqsqrt_63d_base_v109_signal,
    f40ftc_f40_financial_terminal_compounder_tqsqrt_126d_base_v110_signal,
    f40ftc_f40_financial_terminal_compounder_tqsqrt_252d_base_v111_signal,
    f40ftc_f40_financial_terminal_compounder_qclog_21d_base_v112_signal,
    f40ftc_f40_financial_terminal_compounder_qclog_63d_base_v113_signal,
    f40ftc_f40_financial_terminal_compounder_qclog_126d_base_v114_signal,
    f40ftc_f40_financial_terminal_compounder_qclog_252d_base_v115_signal,
    f40ftc_f40_financial_terminal_compounder_tslog_21d_base_v116_signal,
    f40ftc_f40_financial_terminal_compounder_tslog_63d_base_v117_signal,
    f40ftc_f40_financial_terminal_compounder_tslog_126d_base_v118_signal,
    f40ftc_f40_financial_terminal_compounder_tslog_252d_base_v119_signal,
    f40ftc_f40_financial_terminal_compounder_tqlog_21d_base_v120_signal,
    f40ftc_f40_financial_terminal_compounder_tqlog_63d_base_v121_signal,
    f40ftc_f40_financial_terminal_compounder_tqlog_126d_base_v122_signal,
    f40ftc_f40_financial_terminal_compounder_tqlog_252d_base_v123_signal,
    f40ftc_f40_financial_terminal_compounder_qcdiff_21d_base_v124_signal,
    f40ftc_f40_financial_terminal_compounder_qcdiff_63d_base_v125_signal,
    f40ftc_f40_financial_terminal_compounder_qcdiff_126d_base_v126_signal,
    f40ftc_f40_financial_terminal_compounder_tsdiff_21d_base_v127_signal,
    f40ftc_f40_financial_terminal_compounder_tsdiff_63d_base_v128_signal,
    f40ftc_f40_financial_terminal_compounder_tsdiff_126d_base_v129_signal,
    f40ftc_f40_financial_terminal_compounder_tqdiff_21d_base_v130_signal,
    f40ftc_f40_financial_terminal_compounder_tqdiff_63d_base_v131_signal,
    f40ftc_f40_financial_terminal_compounder_tqdiff_126d_base_v132_signal,
    f40ftc_f40_financial_terminal_compounder_qcwt_21d_base_v133_signal,
    f40ftc_f40_financial_terminal_compounder_qcwt_63d_base_v134_signal,
    f40ftc_f40_financial_terminal_compounder_qcwt_126d_base_v135_signal,
    f40ftc_f40_financial_terminal_compounder_qcwt_252d_base_v136_signal,
    f40ftc_f40_financial_terminal_compounder_tswt_21d_base_v137_signal,
    f40ftc_f40_financial_terminal_compounder_tswt_63d_base_v138_signal,
    f40ftc_f40_financial_terminal_compounder_tswt_126d_base_v139_signal,
    f40ftc_f40_financial_terminal_compounder_tswt_252d_base_v140_signal,
    f40ftc_f40_financial_terminal_compounder_tqwt_21d_base_v141_signal,
    f40ftc_f40_financial_terminal_compounder_tqwt_63d_base_v142_signal,
    f40ftc_f40_financial_terminal_compounder_tqwt_126d_base_v143_signal,
    f40ftc_f40_financial_terminal_compounder_tqwt_252d_base_v144_signal,
    f40ftc_f40_financial_terminal_compounder_qcxeqb_21d_base_v145_signal,
    f40ftc_f40_financial_terminal_compounder_qcxeqb_63d_base_v146_signal,
    f40ftc_f40_financial_terminal_compounder_tqxeq_21d_base_v147_signal,
    f40ftc_f40_financial_terminal_compounder_tqxeq_63d_base_v148_signal,
    f40ftc_f40_financial_terminal_compounder_tqxeq_126d_base_v149_signal,
    f40ftc_f40_financial_terminal_compounder_tqxeq_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_FINANCIAL_TERMINAL_COMPOUNDER_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f40_quality_composite", "_f40_terminal_score", "_f40_terminal_quality")
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
    print(f"OK f40_financial_terminal_compounder_base_076_150_claude: {n_features} features pass")
