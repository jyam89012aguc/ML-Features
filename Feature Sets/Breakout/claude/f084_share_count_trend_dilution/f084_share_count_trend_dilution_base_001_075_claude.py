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


def f084sct_f084_share_count_trend_dilution_sch_21d_xclose_base_v001_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_21d_xemac_base_v002_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_21d_xmean_base_v003_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_21d_xclose2_base_v004_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_21d_xmlong_base_v005_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_xclose_base_v006_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_xemac_base_v007_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_xmean_base_v008_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_xclose2_base_v009_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_xmlong_base_v010_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_xclose_base_v011_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_xemac_base_v012_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_xmean_base_v013_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_xclose2_base_v014_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_xmlong_base_v015_signal(sharesbas, closeadj):
    base = _f084_share_change(sharesbas, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_xclose_base_v016_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_xemac_base_v017_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 21), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_xmean_base_v018_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 21), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_xclose2_base_v019_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 21), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_xmlong_base_v020_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 21), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_xclose_base_v021_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_xemac_base_v022_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 63), 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_xmean_base_v023_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 63), 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_xclose2_base_v024_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 63), 126)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_xmlong_base_v025_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 63), 126)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_xclose_base_v026_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_xemac_base_v027_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 252), 504)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_xmean_base_v028_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 252), 504)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_xclose2_base_v029_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 252), 504)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_xmlong_base_v030_signal(sharesbas, closeadj):
    base = _z(_f084_share_change(sharesbas, 252), 504)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_xclose_base_v031_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_xemac_base_v032_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_xmean_base_v033_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 21), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_xclose2_base_v034_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 21), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_xmlong_base_v035_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 21), 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_xclose_base_v036_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_xemac_base_v037_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_xmean_base_v038_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 63), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_xclose2_base_v039_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 63), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_xmlong_base_v040_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 63), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_xclose_base_v041_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_xemac_base_v042_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_xmean_base_v043_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 252), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_xclose2_base_v044_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 252), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_xmlong_base_v045_signal(sharesbas, closeadj):
    base = _ema(_f084_share_change(sharesbas, 252), 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_xclose_base_v046_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_xemac_base_v047_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_xmean_base_v048_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_xclose2_base_v049_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_xmlong_base_v050_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_xclose_base_v051_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_xemac_base_v052_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_xmean_base_v053_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_xclose2_base_v054_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_xmlong_base_v055_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_xclose_base_v056_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_xemac_base_v057_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_xmean_base_v058_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_xclose2_base_v059_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_xmlong_base_v060_signal(sharesbas, closeadj):
    base = _f084_dilution_intensity(sharesbas, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_xclose_base_v061_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_xemac_base_v062_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_xmean_base_v063_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_xclose2_base_v064_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_xmlong_base_v065_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_xclose_base_v066_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_xemac_base_v067_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_xmean_base_v068_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_xclose2_base_v069_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_xmlong_base_v070_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_xclose_base_v071_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_xemac_base_v072_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_xmean_base_v073_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_xclose2_base_v074_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_xmlong_base_v075_signal(sharesbas, closeadj):
    base = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f084sct_f084_share_count_trend_dilution_sch_21d_xclose_base_v001_signal,
    f084sct_f084_share_count_trend_dilution_sch_21d_xemac_base_v002_signal,
    f084sct_f084_share_count_trend_dilution_sch_21d_xmean_base_v003_signal,
    f084sct_f084_share_count_trend_dilution_sch_21d_xclose2_base_v004_signal,
    f084sct_f084_share_count_trend_dilution_sch_21d_xmlong_base_v005_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_xclose_base_v006_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_xemac_base_v007_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_xmean_base_v008_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_xclose2_base_v009_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_xmlong_base_v010_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_xclose_base_v011_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_xemac_base_v012_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_xmean_base_v013_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_xclose2_base_v014_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_xmlong_base_v015_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_xclose_base_v016_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_xemac_base_v017_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_xmean_base_v018_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_xclose2_base_v019_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_xmlong_base_v020_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_xclose_base_v021_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_xemac_base_v022_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_xmean_base_v023_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_xclose2_base_v024_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_xmlong_base_v025_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_xclose_base_v026_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_xemac_base_v027_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_xmean_base_v028_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_xclose2_base_v029_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_xmlong_base_v030_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_xclose_base_v031_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_xemac_base_v032_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_xmean_base_v033_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_xclose2_base_v034_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_xmlong_base_v035_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_xclose_base_v036_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_xemac_base_v037_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_xmean_base_v038_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_xclose2_base_v039_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_xmlong_base_v040_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_xclose_base_v041_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_xemac_base_v042_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_xmean_base_v043_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_xclose2_base_v044_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_xmlong_base_v045_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_xclose_base_v046_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_xemac_base_v047_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_xmean_base_v048_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_xclose2_base_v049_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_xmlong_base_v050_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_xclose_base_v051_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_xemac_base_v052_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_xmean_base_v053_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_xclose2_base_v054_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_xmlong_base_v055_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_xclose_base_v056_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_xemac_base_v057_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_xmean_base_v058_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_xclose2_base_v059_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_xmlong_base_v060_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_xclose_base_v061_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_xemac_base_v062_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_xmean_base_v063_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_xclose2_base_v064_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_xmlong_base_v065_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_xclose_base_v066_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_xemac_base_v067_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_xmean_base_v068_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_xclose2_base_v069_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_xmlong_base_v070_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_xclose_base_v071_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_xemac_base_v072_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_xmean_base_v073_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_xclose2_base_v074_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_xmlong_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F084_SHARE_COUNT_TREND_DILUTION_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f084_share_count_trend_dilution_base_001_075_claude: {n_features} features pass")
