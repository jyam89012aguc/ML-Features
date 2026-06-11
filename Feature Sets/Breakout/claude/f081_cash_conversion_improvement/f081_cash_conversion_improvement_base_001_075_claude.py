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


def f081cci_f081_cash_conversion_improvement_ccmn_21d_xclose_base_v001_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_21d_xemac_base_v002_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_21d_xmean_base_v003_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_21d_xclose2_base_v004_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_21d_xmcap_base_v005_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_xclose_base_v006_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_xemac_base_v007_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_xmean_base_v008_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_xclose2_base_v009_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_xmcap_base_v010_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_xclose_base_v011_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_xemac_base_v012_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_xmean_base_v013_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_xclose2_base_v014_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_xmcap_base_v015_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_xclose_base_v016_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = _std(_f081_cash_conv(ncfo, netinc), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_xemac_base_v017_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = _std(_f081_cash_conv(ncfo, netinc), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_xmean_base_v018_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = _std(_f081_cash_conv(ncfo, netinc), 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_xclose2_base_v019_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = _std(_f081_cash_conv(ncfo, netinc), 21)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_xmcap_base_v020_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = _std(_f081_cash_conv(ncfo, netinc), 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_xclose_base_v021_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = _std(_f081_cash_conv(ncfo, netinc), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_xemac_base_v022_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = _std(_f081_cash_conv(ncfo, netinc), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_xmean_base_v023_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = _std(_f081_cash_conv(ncfo, netinc), 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_xclose2_base_v024_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = _std(_f081_cash_conv(ncfo, netinc), 63)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_xmcap_base_v025_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = _std(_f081_cash_conv(ncfo, netinc), 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_xclose_base_v026_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = _std(_f081_cash_conv(ncfo, netinc), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_xemac_base_v027_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = _std(_f081_cash_conv(ncfo, netinc), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_xmean_base_v028_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = _std(_f081_cash_conv(ncfo, netinc), 252)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_xclose2_base_v029_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = _std(_f081_cash_conv(ncfo, netinc), 252)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_xmcap_base_v030_signal(ncfo, netinc, closeadj):
    base = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = _std(_f081_cash_conv(ncfo, netinc), 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_xclose_base_v031_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_xemac_base_v032_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_xmean_base_v033_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_xclose2_base_v034_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 21)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_xmcap_base_v035_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_xclose_base_v036_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_xemac_base_v037_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_xmean_base_v038_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_xclose2_base_v039_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 63)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_xmcap_base_v040_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_xclose_base_v041_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_xemac_base_v042_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_xmean_base_v043_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 252)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_xclose2_base_v044_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 252)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_xmcap_base_v045_signal(ncfo, netinc, closeadj):
    base = _z(_f081_cash_conv(ncfo, netinc), 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_xclose_base_v046_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_xemac_base_v047_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_xmean_base_v048_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_xclose2_base_v049_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_xmcap_base_v050_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_xclose_base_v051_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_xemac_base_v052_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_xmean_base_v053_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_xclose2_base_v054_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_xmcap_base_v055_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_xclose_base_v056_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_xemac_base_v057_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_xmean_base_v058_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_xclose2_base_v059_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_xmcap_base_v060_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_xclose_base_v061_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_xemac_base_v062_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_xmean_base_v063_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_xclose2_base_v064_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 21)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_xmcap_base_v065_signal(ncfo, ebitda, closeadj, netinc):
    base = _f081_cash_quality(ncfo, ebitda, 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_xclose_base_v066_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_xemac_base_v067_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_xmean_base_v068_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_xclose2_base_v069_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 63)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_xmcap_base_v070_signal(ncfo, ebitda, closeadj, netinc):
    base = _f081_cash_quality(ncfo, ebitda, 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_xclose_base_v071_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_xemac_base_v072_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_xmean_base_v073_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 252)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_xclose2_base_v074_signal(ncfo, ebitda, closeadj):
    base = _f081_cash_quality(ncfo, ebitda, 252)
    result = base * closeadj * closeadj.pct_change(5).fillna(0).add(1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_xmcap_base_v075_signal(ncfo, ebitda, closeadj, netinc):
    base = _f081_cash_quality(ncfo, ebitda, 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f081cci_f081_cash_conversion_improvement_ccmn_21d_xclose_base_v001_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_21d_xemac_base_v002_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_21d_xmean_base_v003_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_21d_xclose2_base_v004_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_21d_xmcap_base_v005_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_xclose_base_v006_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_xemac_base_v007_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_xmean_base_v008_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_xclose2_base_v009_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_xmcap_base_v010_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_xclose_base_v011_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_xemac_base_v012_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_xmean_base_v013_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_xclose2_base_v014_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_xmcap_base_v015_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_xclose_base_v016_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_xemac_base_v017_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_xmean_base_v018_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_xclose2_base_v019_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_xmcap_base_v020_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_xclose_base_v021_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_xemac_base_v022_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_xmean_base_v023_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_xclose2_base_v024_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_xmcap_base_v025_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_xclose_base_v026_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_xemac_base_v027_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_xmean_base_v028_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_xclose2_base_v029_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_xmcap_base_v030_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_xclose_base_v031_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_xemac_base_v032_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_xmean_base_v033_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_xclose2_base_v034_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_xmcap_base_v035_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_xclose_base_v036_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_xemac_base_v037_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_xmean_base_v038_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_xclose2_base_v039_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_xmcap_base_v040_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_xclose_base_v041_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_xemac_base_v042_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_xmean_base_v043_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_xclose2_base_v044_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_xmcap_base_v045_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_xclose_base_v046_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_xemac_base_v047_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_xmean_base_v048_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_xclose2_base_v049_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_xmcap_base_v050_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_xclose_base_v051_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_xemac_base_v052_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_xmean_base_v053_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_xclose2_base_v054_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_xmcap_base_v055_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_xclose_base_v056_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_xemac_base_v057_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_xmean_base_v058_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_xclose2_base_v059_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_xmcap_base_v060_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_xclose_base_v061_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_xemac_base_v062_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_xmean_base_v063_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_xclose2_base_v064_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_xmcap_base_v065_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_xclose_base_v066_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_xemac_base_v067_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_xmean_base_v068_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_xclose2_base_v069_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_xmcap_base_v070_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_xclose_base_v071_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_xemac_base_v072_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_xmean_base_v073_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_xclose2_base_v074_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_xmcap_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F081_CASH_CONVERSION_IMPROVEMENT_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f081_cash_conversion_improvement_base_001_075_claude: {n_features} features pass")
