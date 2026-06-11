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
def _f31_ocf_to_ebitda(ncfo, ebitda):
    return ncfo / ebitda.replace(0, np.nan)


def _f31_cash_conv_durability(ncfo, ebitda, w):
    ratio = ncfo / ebitda.replace(0, np.nan)
    return _mean(ratio, w) / (_std(ratio, w).replace(0, np.nan))


def _f31_conversion_consistency(fcf, ebitda, w):
    ratio = fcf / ebitda.replace(0, np.nan)
    return _mean(ratio, w) - _std(ratio, w)


# ---- features ----

def f31ccq_f31_cash_conversion_quality_ocfebitda_base_v001_signal(ncfo, ebitda, closeadj):
    result = _f31_ocf_to_ebitda(ncfo, ebitda) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitda_21d_base_v002_signal(ncfo, ebitda, closeadj):
    result = _mean(_f31_ocf_to_ebitda(ncfo, ebitda), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitda_63d_base_v003_signal(ncfo, ebitda, closeadj):
    result = _mean(_f31_ocf_to_ebitda(ncfo, ebitda), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitda_126d_base_v004_signal(ncfo, ebitda, closeadj):
    result = _mean(_f31_ocf_to_ebitda(ncfo, ebitda), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitda_252d_base_v005_signal(ncfo, ebitda, closeadj):
    result = _mean(_f31_ocf_to_ebitda(ncfo, ebitda), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitda_504d_base_v006_signal(ncfo, ebitda, closeadj):
    result = _mean(_f31_ocf_to_ebitda(ncfo, ebitda), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdastd_21d_base_v007_signal(ncfo, ebitda, closeadj):
    result = _std(_f31_ocf_to_ebitda(ncfo, ebitda), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdastd_63d_base_v008_signal(ncfo, ebitda, closeadj):
    result = _std(_f31_ocf_to_ebitda(ncfo, ebitda), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdastd_252d_base_v009_signal(ncfo, ebitda, closeadj):
    result = _std(_f31_ocf_to_ebitda(ncfo, ebitda), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaz_63d_base_v010_signal(ncfo, ebitda, closeadj):
    result = _z(_f31_ocf_to_ebitda(ncfo, ebitda), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaz_252d_base_v011_signal(ncfo, ebitda, closeadj):
    result = _z(_f31_ocf_to_ebitda(ncfo, ebitda), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaz_504d_base_v012_signal(ncfo, ebitda, closeadj):
    result = _z(_f31_ocf_to_ebitda(ncfo, ebitda), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_21d_base_v013_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_63d_base_v014_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_126d_base_v015_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_252d_base_v016_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_504d_base_v017_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitda_base_v018_signal(fcf, ebitda, closeadj):
    result = (fcf / ebitda.replace(0, np.nan)) * closeadj + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitda_21d_base_v019_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _mean(base, 21) * closeadj + _f31_conversion_consistency(fcf, ebitda, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitda_63d_base_v020_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _mean(base, 63) * closeadj + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitda_252d_base_v021_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _mean(base, 252) * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_21d_base_v022_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_63d_base_v023_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_126d_base_v024_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_252d_base_v025_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_504d_base_v026_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaema_21d_base_v027_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaema_63d_base_v028_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaema_252d_base_v029_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfminusebitda_base_v030_signal(ncfo, ebitda, closeadj):
    base = ncfo - ebitda
    result = base * closeadj / ebitda.replace(0, np.nan).abs() + _f31_ocf_to_ebitda(ncfo, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfminusebitda_63d_base_v031_signal(ncfo, ebitda, closeadj):
    base = ncfo - ebitda
    result = _mean(base, 63) * closeadj / ebitda.replace(0, np.nan).abs() + _f31_ocf_to_ebitda(ncfo, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfminusebitda_252d_base_v032_signal(ncfo, ebitda, closeadj):
    base = ncfo - ebitda
    result = _mean(base, 252) * closeadj / ebitda.replace(0, np.nan).abs() + _f31_ocf_to_ebitda(ncfo, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfminusebitda_base_v033_signal(fcf, ebitda, closeadj):
    base = fcf - ebitda
    result = base * closeadj / ebitda.replace(0, np.nan).abs() + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfminusebitda_63d_base_v034_signal(fcf, ebitda, closeadj):
    base = fcf - ebitda
    result = _mean(base, 63) * closeadj / ebitda.replace(0, np.nan).abs() + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfminusebitda_252d_base_v035_signal(fcf, ebitda, closeadj):
    base = fcf - ebitda
    result = _mean(base, 252) * closeadj / ebitda.replace(0, np.nan).abs() + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilityratio_21d_base_v036_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 21) * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilityratio_63d_base_v037_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 63) * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilityratio_252d_base_v038_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 252) * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistz_63d_base_v039_signal(fcf, ebitda, closeadj):
    base = _f31_conversion_consistency(fcf, ebitda, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistz_252d_base_v040_signal(fcf, ebitda, closeadj):
    base = _f31_conversion_consistency(fcf, ebitda, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxcurdv_21d_base_v041_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = base * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxcurdv_63d_base_v042_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = base * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitda_diff63_base_v043_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitda_diff252_base_v044_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitda_diff504_base_v045_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = (base - base.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilitydiff_63d_base_v046_signal(ncfo, ebitda, closeadj):
    base = _f31_cash_conv_durability(ncfo, ebitda, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilitydiff_252d_base_v047_signal(ncfo, ebitda, closeadj):
    base = _f31_cash_conv_durability(ncfo, ebitda, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistdiff_63d_base_v048_signal(fcf, ebitda, closeadj):
    base = _f31_conversion_consistency(fcf, ebitda, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistdiff_252d_base_v049_signal(fcf, ebitda, closeadj):
    base = _f31_conversion_consistency(fcf, ebitda, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdaema_21d_base_v050_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj + _f31_conversion_consistency(fcf, ebitda, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdaema_63d_base_v051_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdaema_252d_base_v052_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdastd_21d_base_v053_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _std(base, 21) * closeadj + _f31_conversion_consistency(fcf, ebitda, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdastd_63d_base_v054_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _std(base, 63) * closeadj + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdastd_252d_base_v055_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _std(base, 252) * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdaz_63d_base_v056_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _z(base, 252) * closeadj + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdaz_252d_base_v057_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _z(base, 504) * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaratio_63v252_base_v058_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base, 63) / _mean(base, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaratio_21v63_base_v059_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base, 21) / _mean(base, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaratio_252v504_base_v060_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base, 252) / _mean(base, 504).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdarank_63d_base_v061_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    rank = base.rolling(63, min_periods=20).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdarank_252d_base_v062_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdarank_504d_base_v063_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistxprice_63d_base_v064_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistxprice_252d_base_v065_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabxprice_63d_base_v066_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabxprice_252d_base_v067_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaminusone_63d_base_v068_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda) - 1.0
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaminusone_252d_base_v069_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda) - 1.0
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdasq_63d_base_v070_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base * base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdasq_252d_base_v071_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base * base.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdamax_252d_base_v072_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdamin_252d_base_v073_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdarange_252d_base_v074_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxclose_504d_base_v075_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31ccq_f31_cash_conversion_quality_ocfebitda_base_v001_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitda_21d_base_v002_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitda_63d_base_v003_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitda_126d_base_v004_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitda_252d_base_v005_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitda_504d_base_v006_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdastd_21d_base_v007_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdastd_63d_base_v008_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdastd_252d_base_v009_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaz_63d_base_v010_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaz_252d_base_v011_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaz_504d_base_v012_signal,
    f31ccq_f31_cash_conversion_quality_durability_21d_base_v013_signal,
    f31ccq_f31_cash_conversion_quality_durability_63d_base_v014_signal,
    f31ccq_f31_cash_conversion_quality_durability_126d_base_v015_signal,
    f31ccq_f31_cash_conversion_quality_durability_252d_base_v016_signal,
    f31ccq_f31_cash_conversion_quality_durability_504d_base_v017_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitda_base_v018_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitda_21d_base_v019_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitda_63d_base_v020_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitda_252d_base_v021_signal,
    f31ccq_f31_cash_conversion_quality_consist_21d_base_v022_signal,
    f31ccq_f31_cash_conversion_quality_consist_63d_base_v023_signal,
    f31ccq_f31_cash_conversion_quality_consist_126d_base_v024_signal,
    f31ccq_f31_cash_conversion_quality_consist_252d_base_v025_signal,
    f31ccq_f31_cash_conversion_quality_consist_504d_base_v026_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaema_21d_base_v027_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaema_63d_base_v028_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaema_252d_base_v029_signal,
    f31ccq_f31_cash_conversion_quality_ocfminusebitda_base_v030_signal,
    f31ccq_f31_cash_conversion_quality_ocfminusebitda_63d_base_v031_signal,
    f31ccq_f31_cash_conversion_quality_ocfminusebitda_252d_base_v032_signal,
    f31ccq_f31_cash_conversion_quality_fcfminusebitda_base_v033_signal,
    f31ccq_f31_cash_conversion_quality_fcfminusebitda_63d_base_v034_signal,
    f31ccq_f31_cash_conversion_quality_fcfminusebitda_252d_base_v035_signal,
    f31ccq_f31_cash_conversion_quality_durabilityratio_21d_base_v036_signal,
    f31ccq_f31_cash_conversion_quality_durabilityratio_63d_base_v037_signal,
    f31ccq_f31_cash_conversion_quality_durabilityratio_252d_base_v038_signal,
    f31ccq_f31_cash_conversion_quality_consistz_63d_base_v039_signal,
    f31ccq_f31_cash_conversion_quality_consistz_252d_base_v040_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxcurdv_21d_base_v041_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxcurdv_63d_base_v042_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitda_diff63_base_v043_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitda_diff252_base_v044_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitda_diff504_base_v045_signal,
    f31ccq_f31_cash_conversion_quality_durabilitydiff_63d_base_v046_signal,
    f31ccq_f31_cash_conversion_quality_durabilitydiff_252d_base_v047_signal,
    f31ccq_f31_cash_conversion_quality_consistdiff_63d_base_v048_signal,
    f31ccq_f31_cash_conversion_quality_consistdiff_252d_base_v049_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdaema_21d_base_v050_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdaema_63d_base_v051_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdaema_252d_base_v052_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdastd_21d_base_v053_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdastd_63d_base_v054_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdastd_252d_base_v055_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdaz_63d_base_v056_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdaz_252d_base_v057_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaratio_63v252_base_v058_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaratio_21v63_base_v059_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaratio_252v504_base_v060_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdarank_63d_base_v061_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdarank_252d_base_v062_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdarank_504d_base_v063_signal,
    f31ccq_f31_cash_conversion_quality_consistxprice_63d_base_v064_signal,
    f31ccq_f31_cash_conversion_quality_consistxprice_252d_base_v065_signal,
    f31ccq_f31_cash_conversion_quality_durabxprice_63d_base_v066_signal,
    f31ccq_f31_cash_conversion_quality_durabxprice_252d_base_v067_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaminusone_63d_base_v068_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaminusone_252d_base_v069_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdasq_63d_base_v070_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdasq_252d_base_v071_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdamax_252d_base_v072_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdamin_252d_base_v073_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdarange_252d_base_v074_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxclose_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_CASH_CONVERSION_QUALITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")

    cols = {
        "closeadj": closeadj, "ebitda": ebitda, "fcf": fcf, "ncfo": ncfo,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_ocf_to_ebitda", "_f31_cash_conv_durability", "_f31_conversion_consistency")
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
    print(f"OK f31_cash_conversion_quality_base_001_075_claude: {n_features} features pass")
