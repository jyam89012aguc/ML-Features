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
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f081_cash_conv(ncfo, netinc):
    return ncfo / netinc.abs().replace(0, np.nan)


def _f081_cash_conv_trend(ncfo, netinc, w):
    cc = ncfo / netinc.abs().replace(0, np.nan)
    return cc.rolling(w, min_periods=max(1, w // 2)).mean()


def _f081_cash_quality(ncfo, ebitda, w):
    cq = ncfo / ebitda.abs().replace(0, np.nan)
    return cq.rolling(w, min_periods=max(1, w // 2)).mean()


def f081cci_f081_cash_conversion_improvement_cqz_21d_xclose_base_v076_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_21d_xemac_base_v077_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_21d_xmean_base_v078_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_21d_xclose2_base_v079_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_21d_xmcap_base_v080_signal(ncfo, ebitda, closeadj, netinc):
    base = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_xclose_base_v081_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_xemac_base_v082_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_xmean_base_v083_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_xclose2_base_v084_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_xmcap_base_v085_signal(ncfo, ebitda, closeadj, netinc):
    base = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_xclose_base_v086_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_xemac_base_v087_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_xmean_base_v088_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_xclose2_base_v089_signal(ncfo, ebitda, closeadj):
    base = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_xmcap_base_v090_signal(ncfo, ebitda, closeadj, netinc):
    base = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_xclose_base_v091_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_xemac_base_v092_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_xmean_base_v093_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_xclose2_base_v094_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_xmcap_base_v095_signal(ncfo, ebitda, closeadj, netinc):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_xclose_base_v096_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_xemac_base_v097_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_xmean_base_v098_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_xclose2_base_v099_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_xmcap_base_v100_signal(ncfo, ebitda, closeadj, netinc):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_xclose_base_v101_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_xemac_base_v102_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_xmean_base_v103_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_xclose2_base_v104_signal(ncfo, ebitda, closeadj):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_xmcap_base_v105_signal(ncfo, ebitda, closeadj, netinc):
    base = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_xclose_base_v106_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_xemac_base_v107_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_xmean_base_v108_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_xclose2_base_v109_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_xmcap_base_v110_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_xclose_base_v111_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_xemac_base_v112_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_xmean_base_v113_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_xclose2_base_v114_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_xmcap_base_v115_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_xclose_base_v116_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_xemac_base_v117_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_xmean_base_v118_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_xclose2_base_v119_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_xmcap_base_v120_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_xclose_base_v121_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_xemac_base_v122_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_xmean_base_v123_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_xclose2_base_v124_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_xmcap_base_v125_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_xclose_base_v126_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_xemac_base_v127_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_xmean_base_v128_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_xclose2_base_v129_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_xmcap_base_v130_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_xclose_base_v131_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_xemac_base_v132_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_xmean_base_v133_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_xclose2_base_v134_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_xmcap_base_v135_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_xclose_base_v136_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_xemac_base_v137_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_xmean_base_v138_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_xclose2_base_v139_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_xmcap_base_v140_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_xclose_base_v141_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_xemac_base_v142_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_xmean_base_v143_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_xclose2_base_v144_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_xmcap_base_v145_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_xclose_base_v146_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_xemac_base_v147_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_xmean_base_v148_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_xclose2_base_v149_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_xmcap_base_v150_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base = np.log(cc.replace(0, np.nan) + 1.0)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f081cci_f081_cash_conversion_improvement_cqz_21d_xclose_base_v076_signal,
    f081cci_f081_cash_conversion_improvement_cqz_21d_xemac_base_v077_signal,
    f081cci_f081_cash_conversion_improvement_cqz_21d_xmean_base_v078_signal,
    f081cci_f081_cash_conversion_improvement_cqz_21d_xclose2_base_v079_signal,
    f081cci_f081_cash_conversion_improvement_cqz_21d_xmcap_base_v080_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_xclose_base_v081_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_xemac_base_v082_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_xmean_base_v083_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_xclose2_base_v084_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_xmcap_base_v085_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_xclose_base_v086_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_xemac_base_v087_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_xmean_base_v088_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_xclose2_base_v089_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_xmcap_base_v090_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_xclose_base_v091_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_xemac_base_v092_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_xmean_base_v093_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_xclose2_base_v094_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_xmcap_base_v095_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_xclose_base_v096_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_xemac_base_v097_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_xmean_base_v098_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_xclose2_base_v099_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_xmcap_base_v100_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_xclose_base_v101_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_xemac_base_v102_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_xmean_base_v103_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_xclose2_base_v104_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_xmcap_base_v105_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_xclose_base_v106_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_xemac_base_v107_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_xmean_base_v108_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_xclose2_base_v109_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_xmcap_base_v110_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_xclose_base_v111_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_xemac_base_v112_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_xmean_base_v113_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_xclose2_base_v114_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_xmcap_base_v115_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_xclose_base_v116_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_xemac_base_v117_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_xmean_base_v118_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_xclose2_base_v119_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_xmcap_base_v120_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_xclose_base_v121_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_xemac_base_v122_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_xmean_base_v123_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_xclose2_base_v124_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_xmcap_base_v125_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_xclose_base_v126_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_xemac_base_v127_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_xmean_base_v128_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_xclose2_base_v129_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_xmcap_base_v130_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_xclose_base_v131_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_xemac_base_v132_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_xmean_base_v133_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_xclose2_base_v134_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_xmcap_base_v135_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_xclose_base_v136_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_xemac_base_v137_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_xmean_base_v138_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_xclose2_base_v139_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_xmcap_base_v140_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_xclose_base_v141_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_xemac_base_v142_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_xmean_base_v143_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_xclose2_base_v144_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_xmcap_base_v145_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_xclose_base_v146_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_xemac_base_v147_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_xmean_base_v148_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_xclose2_base_v149_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_xmcap_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F081_CASH_CONVERSION_IMPROVEMENT_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity  = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "netinc": netinc,
        "fcf": fcf, "ncfo": ncfo, "cashneq": cashneq, "debt": debt, "equity": equity,
        "sharesbas": sharesbas, "shareswa": shareswa, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f081_cash_conv", "_f081_cash_conv_trend", "_f081_cash_quality")
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
    print(f"OK f081_cash_conversion_improvement_base_076_150_claude: {n_features} features pass")
