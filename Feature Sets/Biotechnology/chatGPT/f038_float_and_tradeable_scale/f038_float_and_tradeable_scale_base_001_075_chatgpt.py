"""Family f038 - Tradeable share scale and liquidity proxy (Dilution and Share Count) | Sharadar tables: SF1,SEP | fields: sharesbas, volume, close, closeadj | base 001-075"""
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
def _float_and_tradeable_scale_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _float_and_tradeable_scale_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _float_and_tradeable_scale_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_raw_21d_base_v001_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_raw_63d_base_v002_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_raw_126d_base_v003_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_raw_252d_base_v004_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_raw_504d_base_v005_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(sharesbas) times closeadj
def fats_f038_float_and_tradeable_scale_log_21d_base_v006_signal(sharesbas, closeadj):
    result = _mean(_float_and_tradeable_scale_log(sharesbas), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(sharesbas) times closeadj
def fats_f038_float_and_tradeable_scale_log_63d_base_v007_signal(sharesbas, closeadj):
    result = _mean(_float_and_tradeable_scale_log(sharesbas), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(sharesbas) times closeadj
def fats_f038_float_and_tradeable_scale_log_126d_base_v008_signal(sharesbas, closeadj):
    result = _mean(_float_and_tradeable_scale_log(sharesbas), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(sharesbas) times closeadj
def fats_f038_float_and_tradeable_scale_log_252d_base_v009_signal(sharesbas, closeadj):
    result = _mean(_float_and_tradeable_scale_log(sharesbas), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(sharesbas) times closeadj
def fats_f038_float_and_tradeable_scale_log_504d_base_v010_signal(sharesbas, closeadj):
    result = _mean(_float_and_tradeable_scale_log(sharesbas), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/volume mean
def fats_f038_float_and_tradeable_scale_per_volume_63d_base_v011_signal(sharesbas, volume):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, volume), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/volume mean
def fats_f038_float_and_tradeable_scale_per_volume_252d_base_v012_signal(sharesbas, volume):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, volume), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/volume mean
def fats_f038_float_and_tradeable_scale_per_volume_504d_base_v013_signal(sharesbas, volume):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, volume), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/close mean
def fats_f038_float_and_tradeable_scale_per_close_63d_base_v014_signal(sharesbas, close):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, close), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/close mean
def fats_f038_float_and_tradeable_scale_per_close_252d_base_v015_signal(sharesbas, close):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, close), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/close mean
def fats_f038_float_and_tradeable_scale_per_close_504d_base_v016_signal(sharesbas, close):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, close), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/closeadj mean
def fats_f038_float_and_tradeable_scale_per_closeadj_63d_base_v017_signal(sharesbas, closeadj):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, closeadj), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/closeadj mean
def fats_f038_float_and_tradeable_scale_per_closeadj_252d_base_v018_signal(sharesbas, closeadj):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, closeadj), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/closeadj mean
def fats_f038_float_and_tradeable_scale_per_closeadj_504d_base_v019_signal(sharesbas, closeadj):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, closeadj), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/assets mean
def fats_f038_float_and_tradeable_scale_per_assets_63d_base_v020_signal(sharesbas, assets):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/assets mean
def fats_f038_float_and_tradeable_scale_per_assets_252d_base_v021_signal(sharesbas, assets):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/assets mean
def fats_f038_float_and_tradeable_scale_per_assets_504d_base_v022_signal(sharesbas, assets):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/marketcap mean
def fats_f038_float_and_tradeable_scale_per_marketcap_63d_base_v023_signal(sharesbas, marketcap):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/marketcap mean
def fats_f038_float_and_tradeable_scale_per_marketcap_252d_base_v024_signal(sharesbas, marketcap):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/marketcap mean
def fats_f038_float_and_tradeable_scale_per_marketcap_504d_base_v025_signal(sharesbas, marketcap):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sharesbas per share times closeadj
def fats_f038_float_and_tradeable_scale_pershare_21d_base_v026_signal(sharesbas, closeadj):
    ps = _float_and_tradeable_scale_per_share(sharesbas, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas per share times closeadj
def fats_f038_float_and_tradeable_scale_pershare_63d_base_v027_signal(sharesbas, closeadj):
    ps = _float_and_tradeable_scale_per_share(sharesbas, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sharesbas per share times closeadj
def fats_f038_float_and_tradeable_scale_pershare_126d_base_v028_signal(sharesbas, closeadj):
    ps = _float_and_tradeable_scale_per_share(sharesbas, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas per share times closeadj
def fats_f038_float_and_tradeable_scale_pershare_252d_base_v029_signal(sharesbas, closeadj):
    ps = _float_and_tradeable_scale_per_share(sharesbas, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas per share times closeadj
def fats_f038_float_and_tradeable_scale_pershare_504d_base_v030_signal(sharesbas, closeadj):
    ps = _float_and_tradeable_scale_per_share(sharesbas, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_std_63d_base_v031_signal(sharesbas, closeadj):
    result = _std(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_std_252d_base_v032_signal(sharesbas, closeadj):
    result = _std(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_std_504d_base_v033_signal(sharesbas, closeadj):
    result = _std(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of sharesbas
def fats_f038_float_and_tradeable_scale_z_252d_base_v034_signal(sharesbas):
    result = _z(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of sharesbas
def fats_f038_float_and_tradeable_scale_z_504d_base_v035_signal(sharesbas):
    result = _z(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(sharesbas)
def fats_f038_float_and_tradeable_scale_logz_252d_base_v036_signal(sharesbas):
    result = _z(_float_and_tradeable_scale_log(sharesbas), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(sharesbas)
def fats_f038_float_and_tradeable_scale_logz_504d_base_v037_signal(sharesbas):
    result = _z(_float_and_tradeable_scale_log(sharesbas), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sharesbas^2 times closeadj
def fats_f038_float_and_tradeable_scale_sq_63d_base_v038_signal(sharesbas, closeadj):
    result = _mean(sharesbas * sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sharesbas^2 times closeadj
def fats_f038_float_and_tradeable_scale_sq_252d_base_v039_signal(sharesbas, closeadj):
    result = _mean(sharesbas * sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(sharesbas) times closeadj
def fats_f038_float_and_tradeable_scale_sign_21d_base_v040_signal(sharesbas, closeadj):
    result = _mean(np.sign(sharesbas), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(sharesbas) times closeadj
def fats_f038_float_and_tradeable_scale_sign_63d_base_v041_signal(sharesbas, closeadj):
    result = _mean(np.sign(sharesbas), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(sharesbas) times closeadj
def fats_f038_float_and_tradeable_scale_sign_252d_base_v042_signal(sharesbas, closeadj):
    result = _mean(np.sign(sharesbas), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/opex mean
def fats_f038_float_and_tradeable_scale_per_opex_63d_base_v043_signal(sharesbas, opex):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/opex mean
def fats_f038_float_and_tradeable_scale_per_opex_252d_base_v044_signal(sharesbas, opex):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/ebitda mean
def fats_f038_float_and_tradeable_scale_per_ebitda_63d_base_v045_signal(sharesbas, ebitda):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/ebitda mean
def fats_f038_float_and_tradeable_scale_per_ebitda_252d_base_v046_signal(sharesbas, ebitda):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/capex mean
def fats_f038_float_and_tradeable_scale_per_capex_63d_base_v047_signal(sharesbas, capex):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/capex mean
def fats_f038_float_and_tradeable_scale_per_capex_252d_base_v048_signal(sharesbas, capex):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/liabilities mean
def fats_f038_float_and_tradeable_scale_per_liabilities_63d_base_v049_signal(sharesbas, liabilities):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/liabilities mean
def fats_f038_float_and_tradeable_scale_per_liabilities_252d_base_v050_signal(sharesbas, liabilities):
    result = _mean(_float_and_tradeable_scale_scaled(sharesbas, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 252d max times closeadj
def fats_f038_float_and_tradeable_scale_relmax_252d_base_v051_signal(sharesbas, closeadj):
    peak = sharesbas.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (sharesbas / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 504d max times closeadj
def fats_f038_float_and_tradeable_scale_relmax_504d_base_v052_signal(sharesbas, closeadj):
    peak = sharesbas.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (sharesbas / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 252d min times closeadj
def fats_f038_float_and_tradeable_scale_relmin_252d_base_v053_signal(sharesbas, closeadj):
    trough = sharesbas.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (sharesbas / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 504d min times closeadj
def fats_f038_float_and_tradeable_scale_relmin_504d_base_v054_signal(sharesbas, closeadj):
    trough = sharesbas.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (sharesbas / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_pct_21d_base_v055_signal(sharesbas, closeadj):
    result = _pct_change(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_pct_63d_base_v056_signal(sharesbas, closeadj):
    result = _pct_change(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_pct_252d_base_v057_signal(sharesbas, closeadj):
    result = _pct_change(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_sum_63d_base_v058_signal(sharesbas, closeadj):
    result = sharesbas.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_sum_252d_base_v059_signal(sharesbas, closeadj):
    result = sharesbas.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_sum_504d_base_v060_signal(sharesbas, closeadj):
    result = sharesbas.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(63d) / smoothed volume(252d) x closeadj
def fats_f038_float_and_tradeable_scale_rom_volume_252_63d_base_v061_signal(sharesbas, volume, closeadj):
    n = _mean(sharesbas, 63)
    d = _mean(volume, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(126d) / smoothed volume(504d) x closeadj
def fats_f038_float_and_tradeable_scale_rom_volume_504_126d_base_v062_signal(sharesbas, volume, closeadj):
    n = _mean(sharesbas, 126)
    d = _mean(volume, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(63d) / smoothed close(252d) x closeadj
def fats_f038_float_and_tradeable_scale_rom_close_252_63d_base_v063_signal(sharesbas, close, closeadj):
    n = _mean(sharesbas, 63)
    d = _mean(close, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(126d) / smoothed close(504d) x closeadj
def fats_f038_float_and_tradeable_scale_rom_close_504_126d_base_v064_signal(sharesbas, close, closeadj):
    n = _mean(sharesbas, 126)
    d = _mean(close, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(63d) / smoothed closeadj(252d) x closeadj
def fats_f038_float_and_tradeable_scale_rom_closeadj_252_63d_base_v065_signal(sharesbas, closeadj):
    n = _mean(sharesbas, 63)
    d = _mean(closeadj, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(126d) / smoothed closeadj(504d) x closeadj
def fats_f038_float_and_tradeable_scale_rom_closeadj_504_126d_base_v066_signal(sharesbas, closeadj):
    n = _mean(sharesbas, 126)
    d = _mean(closeadj, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sharesbas) / std(volume)
def fats_f038_float_and_tradeable_scale_volratio_volume_252d_base_v067_signal(sharesbas, volume):
    n = _std(sharesbas, 252)
    d = _std(volume, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sharesbas) / std(volume)
def fats_f038_float_and_tradeable_scale_volratio_volume_504d_base_v068_signal(sharesbas, volume):
    n = _std(sharesbas, 504)
    d = _std(volume, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sharesbas) / std(close)
def fats_f038_float_and_tradeable_scale_volratio_close_252d_base_v069_signal(sharesbas, close):
    n = _std(sharesbas, 252)
    d = _std(close, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sharesbas) / std(close)
def fats_f038_float_and_tradeable_scale_volratio_close_504d_base_v070_signal(sharesbas, close):
    n = _std(sharesbas, 504)
    d = _std(close, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_raw_5d_base_v071_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed sharesbas times closeadj
def fats_f038_float_and_tradeable_scale_raw_1008d_base_v072_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sharesbas/volume
def fats_f038_float_and_tradeable_scale_log_per_volume_252d_base_v073_signal(sharesbas, volume):
    s = _float_and_tradeable_scale_scaled(sharesbas, volume)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sharesbas/volume
def fats_f038_float_and_tradeable_scale_log_per_volume_504d_base_v074_signal(sharesbas, volume):
    s = _float_and_tradeable_scale_scaled(sharesbas, volume)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sharesbas/close
def fats_f038_float_and_tradeable_scale_log_per_close_252d_base_v075_signal(sharesbas, close):
    s = _float_and_tradeable_scale_scaled(sharesbas, close)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
