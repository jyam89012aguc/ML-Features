"""Family f53 - Margin improvement rate  (H_Margins) | 2nd derivatives 001-150"""
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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _margin_improvement_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _margin_improvement_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _margin_improvement_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw grossmargin
def mi_f53_margin_improvement_raw_21d_slope_v001_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw grossmargin
def mi_f53_margin_improvement_raw_21d_slope_v002_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw grossmargin
def mi_f53_margin_improvement_raw_21d_slope_v003_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw grossmargin
def mi_f53_margin_improvement_raw_63d_slope_v004_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw grossmargin
def mi_f53_margin_improvement_raw_63d_slope_v005_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw grossmargin
def mi_f53_margin_improvement_raw_63d_slope_v006_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw grossmargin
def mi_f53_margin_improvement_raw_126d_slope_v007_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw grossmargin
def mi_f53_margin_improvement_raw_126d_slope_v008_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw grossmargin
def mi_f53_margin_improvement_raw_126d_slope_v009_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw grossmargin
def mi_f53_margin_improvement_raw_252d_slope_v010_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw grossmargin
def mi_f53_margin_improvement_raw_252d_slope_v011_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw grossmargin
def mi_f53_margin_improvement_raw_252d_slope_v012_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw grossmargin
def mi_f53_margin_improvement_raw_504d_slope_v013_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw grossmargin
def mi_f53_margin_improvement_raw_504d_slope_v014_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw grossmargin
def mi_f53_margin_improvement_raw_504d_slope_v015_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log grossmargin
def mi_f53_margin_improvement_log_21d_slope_v016_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log grossmargin
def mi_f53_margin_improvement_log_21d_slope_v017_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log grossmargin
def mi_f53_margin_improvement_log_21d_slope_v018_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log grossmargin
def mi_f53_margin_improvement_log_63d_slope_v019_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log grossmargin
def mi_f53_margin_improvement_log_63d_slope_v020_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log grossmargin
def mi_f53_margin_improvement_log_63d_slope_v021_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log grossmargin
def mi_f53_margin_improvement_log_126d_slope_v022_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log grossmargin
def mi_f53_margin_improvement_log_126d_slope_v023_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log grossmargin
def mi_f53_margin_improvement_log_126d_slope_v024_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log grossmargin
def mi_f53_margin_improvement_log_252d_slope_v025_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log grossmargin
def mi_f53_margin_improvement_log_252d_slope_v026_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log grossmargin
def mi_f53_margin_improvement_log_252d_slope_v027_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log grossmargin
def mi_f53_margin_improvement_log_504d_slope_v028_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log grossmargin
def mi_f53_margin_improvement_log_504d_slope_v029_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log grossmargin
def mi_f53_margin_improvement_log_504d_slope_v030_signal(grossmargin, closeadj):
    base = _mean(_margin_improvement_log(grossmargin), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare grossmargin
def mi_f53_margin_improvement_pershare_21d_slope_v031_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare grossmargin
def mi_f53_margin_improvement_pershare_21d_slope_v032_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare grossmargin
def mi_f53_margin_improvement_pershare_21d_slope_v033_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare grossmargin
def mi_f53_margin_improvement_pershare_63d_slope_v034_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare grossmargin
def mi_f53_margin_improvement_pershare_63d_slope_v035_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare grossmargin
def mi_f53_margin_improvement_pershare_63d_slope_v036_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare grossmargin
def mi_f53_margin_improvement_pershare_126d_slope_v037_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare grossmargin
def mi_f53_margin_improvement_pershare_126d_slope_v038_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare grossmargin
def mi_f53_margin_improvement_pershare_126d_slope_v039_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare grossmargin
def mi_f53_margin_improvement_pershare_252d_slope_v040_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare grossmargin
def mi_f53_margin_improvement_pershare_252d_slope_v041_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare grossmargin
def mi_f53_margin_improvement_pershare_252d_slope_v042_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare grossmargin
def mi_f53_margin_improvement_pershare_504d_slope_v043_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare grossmargin
def mi_f53_margin_improvement_pershare_504d_slope_v044_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare grossmargin
def mi_f53_margin_improvement_pershare_504d_slope_v045_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_margin_improvement_per_share(grossmargin, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_21d_slope_v046_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_21d_slope_v047_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_21d_slope_v048_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_63d_slope_v049_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_63d_slope_v050_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_63d_slope_v051_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_126d_slope_v052_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_126d_slope_v053_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_126d_slope_v054_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_252d_slope_v055_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_252d_slope_v056_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_252d_slope_v057_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_504d_slope_v058_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_504d_slope_v059_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets grossmargin
def mi_f53_margin_improvement_per_assets_504d_slope_v060_signal(grossmargin, assets):
    base = _mean(_margin_improvement_scaled(grossmargin, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_21d_slope_v061_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_21d_slope_v062_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_21d_slope_v063_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_63d_slope_v064_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_63d_slope_v065_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_63d_slope_v066_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_126d_slope_v067_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_126d_slope_v068_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_126d_slope_v069_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_252d_slope_v070_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_252d_slope_v071_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_252d_slope_v072_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_504d_slope_v073_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_504d_slope_v074_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap grossmargin
def mi_f53_margin_improvement_per_marketcap_504d_slope_v075_signal(grossmargin, marketcap):
    base = _mean(_margin_improvement_scaled(grossmargin, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_21d_slope_v076_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_21d_slope_v077_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_21d_slope_v078_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_63d_slope_v079_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_63d_slope_v080_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_63d_slope_v081_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_126d_slope_v082_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_126d_slope_v083_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_126d_slope_v084_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_252d_slope_v085_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_252d_slope_v086_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_252d_slope_v087_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_504d_slope_v088_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_504d_slope_v089_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity grossmargin
def mi_f53_margin_improvement_per_equity_504d_slope_v090_signal(grossmargin, equity):
    base = _mean(_margin_improvement_scaled(grossmargin, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std grossmargin
def mi_f53_margin_improvement_std_21d_slope_v091_signal(grossmargin, closeadj):
    base = _std(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std grossmargin
def mi_f53_margin_improvement_std_21d_slope_v092_signal(grossmargin, closeadj):
    base = _std(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std grossmargin
def mi_f53_margin_improvement_std_21d_slope_v093_signal(grossmargin, closeadj):
    base = _std(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std grossmargin
def mi_f53_margin_improvement_std_63d_slope_v094_signal(grossmargin, closeadj):
    base = _std(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std grossmargin
def mi_f53_margin_improvement_std_63d_slope_v095_signal(grossmargin, closeadj):
    base = _std(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std grossmargin
def mi_f53_margin_improvement_std_63d_slope_v096_signal(grossmargin, closeadj):
    base = _std(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std grossmargin
def mi_f53_margin_improvement_std_126d_slope_v097_signal(grossmargin, closeadj):
    base = _std(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std grossmargin
def mi_f53_margin_improvement_std_126d_slope_v098_signal(grossmargin, closeadj):
    base = _std(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std grossmargin
def mi_f53_margin_improvement_std_126d_slope_v099_signal(grossmargin, closeadj):
    base = _std(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std grossmargin
def mi_f53_margin_improvement_std_252d_slope_v100_signal(grossmargin, closeadj):
    base = _std(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std grossmargin
def mi_f53_margin_improvement_std_252d_slope_v101_signal(grossmargin, closeadj):
    base = _std(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std grossmargin
def mi_f53_margin_improvement_std_252d_slope_v102_signal(grossmargin, closeadj):
    base = _std(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std grossmargin
def mi_f53_margin_improvement_std_504d_slope_v103_signal(grossmargin, closeadj):
    base = _std(grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std grossmargin
def mi_f53_margin_improvement_std_504d_slope_v104_signal(grossmargin, closeadj):
    base = _std(grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std grossmargin
def mi_f53_margin_improvement_std_504d_slope_v105_signal(grossmargin, closeadj):
    base = _std(grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm grossmargin
def mi_f53_margin_improvement_ewm_21d_slope_v106_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm grossmargin
def mi_f53_margin_improvement_ewm_21d_slope_v107_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm grossmargin
def mi_f53_margin_improvement_ewm_21d_slope_v108_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm grossmargin
def mi_f53_margin_improvement_ewm_63d_slope_v109_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm grossmargin
def mi_f53_margin_improvement_ewm_63d_slope_v110_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm grossmargin
def mi_f53_margin_improvement_ewm_63d_slope_v111_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm grossmargin
def mi_f53_margin_improvement_ewm_126d_slope_v112_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm grossmargin
def mi_f53_margin_improvement_ewm_126d_slope_v113_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm grossmargin
def mi_f53_margin_improvement_ewm_126d_slope_v114_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm grossmargin
def mi_f53_margin_improvement_ewm_252d_slope_v115_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm grossmargin
def mi_f53_margin_improvement_ewm_252d_slope_v116_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm grossmargin
def mi_f53_margin_improvement_ewm_252d_slope_v117_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm grossmargin
def mi_f53_margin_improvement_ewm_504d_slope_v118_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm grossmargin
def mi_f53_margin_improvement_ewm_504d_slope_v119_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm grossmargin
def mi_f53_margin_improvement_ewm_504d_slope_v120_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq grossmargin
def mi_f53_margin_improvement_sq_21d_slope_v121_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq grossmargin
def mi_f53_margin_improvement_sq_21d_slope_v122_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq grossmargin
def mi_f53_margin_improvement_sq_21d_slope_v123_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq grossmargin
def mi_f53_margin_improvement_sq_63d_slope_v124_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq grossmargin
def mi_f53_margin_improvement_sq_63d_slope_v125_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq grossmargin
def mi_f53_margin_improvement_sq_63d_slope_v126_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq grossmargin
def mi_f53_margin_improvement_sq_126d_slope_v127_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq grossmargin
def mi_f53_margin_improvement_sq_126d_slope_v128_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq grossmargin
def mi_f53_margin_improvement_sq_126d_slope_v129_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq grossmargin
def mi_f53_margin_improvement_sq_252d_slope_v130_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq grossmargin
def mi_f53_margin_improvement_sq_252d_slope_v131_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq grossmargin
def mi_f53_margin_improvement_sq_252d_slope_v132_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq grossmargin
def mi_f53_margin_improvement_sq_504d_slope_v133_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq grossmargin
def mi_f53_margin_improvement_sq_504d_slope_v134_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq grossmargin
def mi_f53_margin_improvement_sq_504d_slope_v135_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z grossmargin
def mi_f53_margin_improvement_z_21d_slope_v136_signal(grossmargin):
    base = _z(grossmargin, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z grossmargin
def mi_f53_margin_improvement_z_21d_slope_v137_signal(grossmargin):
    base = _z(grossmargin, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z grossmargin
def mi_f53_margin_improvement_z_21d_slope_v138_signal(grossmargin):
    base = _z(grossmargin, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z grossmargin
def mi_f53_margin_improvement_z_63d_slope_v139_signal(grossmargin):
    base = _z(grossmargin, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z grossmargin
def mi_f53_margin_improvement_z_63d_slope_v140_signal(grossmargin):
    base = _z(grossmargin, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z grossmargin
def mi_f53_margin_improvement_z_63d_slope_v141_signal(grossmargin):
    base = _z(grossmargin, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z grossmargin
def mi_f53_margin_improvement_z_126d_slope_v142_signal(grossmargin):
    base = _z(grossmargin, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z grossmargin
def mi_f53_margin_improvement_z_126d_slope_v143_signal(grossmargin):
    base = _z(grossmargin, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z grossmargin
def mi_f53_margin_improvement_z_126d_slope_v144_signal(grossmargin):
    base = _z(grossmargin, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z grossmargin
def mi_f53_margin_improvement_z_252d_slope_v145_signal(grossmargin):
    base = _z(grossmargin, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z grossmargin
def mi_f53_margin_improvement_z_252d_slope_v146_signal(grossmargin):
    base = _z(grossmargin, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z grossmargin
def mi_f53_margin_improvement_z_252d_slope_v147_signal(grossmargin):
    base = _z(grossmargin, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z grossmargin
def mi_f53_margin_improvement_z_504d_slope_v148_signal(grossmargin):
    base = _z(grossmargin, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z grossmargin
def mi_f53_margin_improvement_z_504d_slope_v149_signal(grossmargin):
    base = _z(grossmargin, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z grossmargin
def mi_f53_margin_improvement_z_504d_slope_v150_signal(grossmargin):
    base = _z(grossmargin, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
