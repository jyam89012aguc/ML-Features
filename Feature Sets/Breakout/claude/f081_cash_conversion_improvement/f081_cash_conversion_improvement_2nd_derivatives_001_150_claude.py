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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f081_cash_conv(ncfo, netinc):
    return ncfo / netinc.abs().replace(0, np.nan)


def _f081_cash_conv_trend(ncfo, netinc, w):
    cc = ncfo / netinc.abs().replace(0, np.nan)
    return cc.rolling(w, min_periods=max(1, w // 2)).mean()


def _f081_cash_quality(ncfo, ebitda, w):
    cq = ncfo / ebitda.abs().replace(0, np.nan)
    return cq.rolling(w, min_periods=max(1, w // 2)).mean()


def f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v001_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v002_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v003_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v004_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v005_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v006_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v007_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v008_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v009_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v010_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v011_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v012_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v013_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v014_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v015_signal(ncfo, netinc, closeadj):
    base_pre = _f081_cash_conv_trend(ncfo, netinc, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v016_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v017_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v018_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v019_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v020_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v021_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v022_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v023_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v024_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v025_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v026_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v027_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v028_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v029_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v030_signal(ncfo, netinc, closeadj):
    base_pre = _std(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v031_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v032_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v033_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v034_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v035_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v036_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v037_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v038_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v039_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v040_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v041_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v042_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v043_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v044_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v045_signal(ncfo, netinc, closeadj):
    base_pre = _z(_f081_cash_conv(ncfo, netinc), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v046_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v047_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v048_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v049_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v050_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 21) + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v051_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v052_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v053_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v054_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v055_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 63) + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v056_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v057_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v058_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v059_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v060_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = _ema(cc, 252) + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v061_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v062_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v063_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v064_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v065_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v066_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v067_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v068_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v069_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v070_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v071_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v072_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v073_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v074_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v075_signal(ncfo, ebitda, closeadj):
    base_pre = _f081_cash_quality(ncfo, ebitda, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v076_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v077_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v078_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v079_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v080_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v081_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v082_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v083_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v084_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v085_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v086_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v087_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v088_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v089_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v090_signal(ncfo, ebitda, closeadj):
    base_pre = _z(_f081_cash_quality(ncfo, ebitda, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v091_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v092_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v093_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v094_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v095_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v096_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v097_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v098_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v099_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v100_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v101_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v102_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v103_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v104_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v105_signal(ncfo, ebitda, closeadj):
    base_pre = _ema(_f081_cash_quality(ncfo, ebitda, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v106_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v107_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v108_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v109_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v110_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v111_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v112_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v113_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v114_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v115_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v116_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v117_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v118_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v119_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v120_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).min() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v121_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v122_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v123_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v124_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v125_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(21, min_periods=max(1, 21//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 21) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v126_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v127_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v128_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v129_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v130_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(63, min_periods=max(1, 63//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 63) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v131_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v132_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v133_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v134_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v135_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv(ncfo, netinc)
    base_pre = cc.rolling(252, min_periods=max(1, 252//2)).max() + _f081_cash_conv_trend(ncfo, netinc, 252) * 0.0
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v136_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v137_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v138_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v139_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v140_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 21).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v141_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v142_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v143_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v144_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v145_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 63).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v146_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v147_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v148_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v149_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v150_signal(ncfo, netinc, closeadj):
    cc = _f081_cash_conv_trend(ncfo, netinc, 252).abs()
    base_pre = np.log(cc.replace(0, np.nan) + 1.0)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v001_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v002_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v003_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v004_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_21d_slope_v005_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v006_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v007_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v008_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v009_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_63d_slope_v010_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v011_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v012_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v013_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v014_signal,
    f081cci_f081_cash_conversion_improvement_ccmn_252d_slope_v015_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v016_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v017_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v018_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v019_signal,
    f081cci_f081_cash_conversion_improvement_ccst_21d_slope_v020_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v021_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v022_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v023_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v024_signal,
    f081cci_f081_cash_conversion_improvement_ccst_63d_slope_v025_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v026_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v027_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v028_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v029_signal,
    f081cci_f081_cash_conversion_improvement_ccst_252d_slope_v030_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v031_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v032_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v033_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v034_signal,
    f081cci_f081_cash_conversion_improvement_ccz_21d_slope_v035_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v036_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v037_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v038_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v039_signal,
    f081cci_f081_cash_conversion_improvement_ccz_63d_slope_v040_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v041_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v042_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v043_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v044_signal,
    f081cci_f081_cash_conversion_improvement_ccz_252d_slope_v045_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v046_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v047_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v048_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v049_signal,
    f081cci_f081_cash_conversion_improvement_ccem_21d_slope_v050_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v051_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v052_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v053_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v054_signal,
    f081cci_f081_cash_conversion_improvement_ccem_63d_slope_v055_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v056_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v057_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v058_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v059_signal,
    f081cci_f081_cash_conversion_improvement_ccem_252d_slope_v060_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v061_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v062_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v063_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v064_signal,
    f081cci_f081_cash_conversion_improvement_cqm_21d_slope_v065_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v066_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v067_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v068_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v069_signal,
    f081cci_f081_cash_conversion_improvement_cqm_63d_slope_v070_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v071_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v072_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v073_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v074_signal,
    f081cci_f081_cash_conversion_improvement_cqm_252d_slope_v075_signal,
    f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v076_signal,
    f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v077_signal,
    f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v078_signal,
    f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v079_signal,
    f081cci_f081_cash_conversion_improvement_cqz_21d_slope_v080_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v081_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v082_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v083_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v084_signal,
    f081cci_f081_cash_conversion_improvement_cqz_63d_slope_v085_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v086_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v087_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v088_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v089_signal,
    f081cci_f081_cash_conversion_improvement_cqz_252d_slope_v090_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v091_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v092_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v093_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v094_signal,
    f081cci_f081_cash_conversion_improvement_cqem_21d_slope_v095_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v096_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v097_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v098_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v099_signal,
    f081cci_f081_cash_conversion_improvement_cqem_63d_slope_v100_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v101_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v102_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v103_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v104_signal,
    f081cci_f081_cash_conversion_improvement_cqem_252d_slope_v105_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v106_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v107_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v108_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v109_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_21d_slope_v110_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v111_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v112_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v113_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v114_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_63d_slope_v115_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v116_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v117_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v118_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v119_signal,
    f081cci_f081_cash_conversion_improvement_ccmin_252d_slope_v120_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v121_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v122_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v123_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v124_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_21d_slope_v125_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v126_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v127_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v128_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v129_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_63d_slope_v130_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v131_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v132_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v133_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v134_signal,
    f081cci_f081_cash_conversion_improvement_ccmax_252d_slope_v135_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v136_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v137_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v138_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v139_signal,
    f081cci_f081_cash_conversion_improvement_cclog_21d_slope_v140_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v141_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v142_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v143_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v144_signal,
    f081cci_f081_cash_conversion_improvement_cclog_63d_slope_v145_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v146_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v147_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v148_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v149_signal,
    f081cci_f081_cash_conversion_improvement_cclog_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F081_CASH_CONVERSION_IMPROVEMENT_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f081_cash_conversion_improvement_2nd_derivatives_001_150_claude: {n_features} features pass")
