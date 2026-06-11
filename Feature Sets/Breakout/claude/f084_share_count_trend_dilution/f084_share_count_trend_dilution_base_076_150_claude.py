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
def _f084_share_change(sharesbas, w):
    return sharesbas.pct_change(periods=w)


def _f084_dilution_intensity(sharesbas, w):
    chg = sharesbas.pct_change(periods=w)
    return chg.rolling(w, min_periods=max(1, w // 2)).std() + chg


def _f084_dilution_score(sharesbas, shareswa, w):
    gap = (sharesbas - shareswa) / shareswa.abs().replace(0, np.nan)
    return gap.rolling(w, min_periods=max(1, w // 2)).mean()


def f084sct_f084_share_count_trend_dilution_dine_21d_xclose_base_v076_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_21d_xemac_base_v077_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_21d_xmean_base_v078_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_21d_xclose2_base_v079_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_21d_xmlong_base_v080_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_xclose_base_v081_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_xemac_base_v082_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_xmean_base_v083_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_xclose2_base_v084_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_xmlong_base_v085_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_xclose_base_v086_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_xemac_base_v087_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_xmean_base_v088_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_xclose2_base_v089_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_xmlong_base_v090_signal(sharesbas, closeadj):
    base = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_xclose_base_v091_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_xemac_base_v092_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_xmean_base_v093_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_xclose2_base_v094_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_xmlong_base_v095_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_xclose_base_v096_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_xemac_base_v097_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_xmean_base_v098_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_xclose2_base_v099_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_xmlong_base_v100_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_xclose_base_v101_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_xemac_base_v102_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_xmean_base_v103_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_xclose2_base_v104_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_xmlong_base_v105_signal(sharesbas, shareswa, closeadj):
    base = _f084_dilution_score(sharesbas, shareswa, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_xclose_base_v106_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_xemac_base_v107_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_xmean_base_v108_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_xclose2_base_v109_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_xmlong_base_v110_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_xclose_base_v111_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_xemac_base_v112_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_xmean_base_v113_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_xclose2_base_v114_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_xmlong_base_v115_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_xclose_base_v116_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_xemac_base_v117_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_xmean_base_v118_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_xclose2_base_v119_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_xmlong_base_v120_signal(sharesbas, shareswa, closeadj):
    base = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_xclose_base_v121_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_xemac_base_v122_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_xmean_base_v123_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_xclose2_base_v124_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_xmlong_base_v125_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_xclose_base_v126_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_xemac_base_v127_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_xmean_base_v128_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_xclose2_base_v129_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_xmlong_base_v130_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_xclose_base_v131_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_xemac_base_v132_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_xmean_base_v133_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_xclose2_base_v134_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_xmlong_base_v135_signal(sharesbas, shareswa, closeadj):
    base = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_xclose_base_v136_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_xemac_base_v137_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_xmean_base_v138_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_xclose2_base_v139_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_xmlong_base_v140_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_xclose_base_v141_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_xemac_base_v142_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_xmean_base_v143_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_xclose2_base_v144_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_xmlong_base_v145_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_xclose_base_v146_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_xemac_base_v147_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_xmean_base_v148_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_xclose2_base_v149_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_xmlong_base_v150_signal(sharesbas, shareswa, closeadj):
    base = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f084sct_f084_share_count_trend_dilution_dine_21d_xclose_base_v076_signal,
    f084sct_f084_share_count_trend_dilution_dine_21d_xemac_base_v077_signal,
    f084sct_f084_share_count_trend_dilution_dine_21d_xmean_base_v078_signal,
    f084sct_f084_share_count_trend_dilution_dine_21d_xclose2_base_v079_signal,
    f084sct_f084_share_count_trend_dilution_dine_21d_xmlong_base_v080_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_xclose_base_v081_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_xemac_base_v082_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_xmean_base_v083_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_xclose2_base_v084_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_xmlong_base_v085_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_xclose_base_v086_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_xemac_base_v087_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_xmean_base_v088_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_xclose2_base_v089_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_xmlong_base_v090_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_xclose_base_v091_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_xemac_base_v092_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_xmean_base_v093_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_xclose2_base_v094_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_xmlong_base_v095_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_xclose_base_v096_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_xemac_base_v097_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_xmean_base_v098_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_xclose2_base_v099_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_xmlong_base_v100_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_xclose_base_v101_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_xemac_base_v102_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_xmean_base_v103_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_xclose2_base_v104_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_xmlong_base_v105_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_xclose_base_v106_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_xemac_base_v107_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_xmean_base_v108_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_xclose2_base_v109_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_xmlong_base_v110_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_xclose_base_v111_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_xemac_base_v112_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_xmean_base_v113_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_xclose2_base_v114_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_xmlong_base_v115_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_xclose_base_v116_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_xemac_base_v117_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_xmean_base_v118_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_xclose2_base_v119_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_xmlong_base_v120_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_xclose_base_v121_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_xemac_base_v122_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_xmean_base_v123_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_xclose2_base_v124_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_xmlong_base_v125_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_xclose_base_v126_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_xemac_base_v127_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_xmean_base_v128_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_xclose2_base_v129_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_xmlong_base_v130_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_xclose_base_v131_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_xemac_base_v132_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_xmean_base_v133_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_xclose2_base_v134_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_xmlong_base_v135_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_xclose_base_v136_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_xemac_base_v137_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_xmean_base_v138_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_xclose2_base_v139_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_xmlong_base_v140_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_xclose_base_v141_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_xemac_base_v142_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_xmean_base_v143_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_xclose2_base_v144_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_xmlong_base_v145_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_xclose_base_v146_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_xemac_base_v147_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_xmean_base_v148_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_xclose2_base_v149_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_xmlong_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F084_SHARE_COUNT_TREND_DILUTION_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f084_share_change", "_f084_dilution_intensity", "_f084_dilution_score")
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
    print(f"OK f084_share_count_trend_dilution_base_076_150_claude: {n_features} features pass")
