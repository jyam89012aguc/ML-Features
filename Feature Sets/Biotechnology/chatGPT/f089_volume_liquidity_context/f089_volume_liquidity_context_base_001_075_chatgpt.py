"""Family f089 - Volume and dollar liquidity context (Market Context from Sharadar Prices) | Sharadar tables: SEP,SFP | fields: volume, close, closeadj, sharesbas | base 001-075"""
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
def _volume_liquidity_context_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _volume_liquidity_context_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _volume_liquidity_context_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed volume times closeadj
def vlc_f089_volume_liquidity_context_raw_21d_base_v001_signal(volume, closeadj):
    result = _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed volume times closeadj
def vlc_f089_volume_liquidity_context_raw_63d_base_v002_signal(volume, closeadj):
    result = _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed volume times closeadj
def vlc_f089_volume_liquidity_context_raw_126d_base_v003_signal(volume, closeadj):
    result = _mean(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed volume times closeadj
def vlc_f089_volume_liquidity_context_raw_252d_base_v004_signal(volume, closeadj):
    result = _mean(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed volume times closeadj
def vlc_f089_volume_liquidity_context_raw_504d_base_v005_signal(volume, closeadj):
    result = _mean(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(volume) times closeadj
def vlc_f089_volume_liquidity_context_log_21d_base_v006_signal(volume, closeadj):
    result = _mean(_volume_liquidity_context_log(volume), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(volume) times closeadj
def vlc_f089_volume_liquidity_context_log_63d_base_v007_signal(volume, closeadj):
    result = _mean(_volume_liquidity_context_log(volume), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(volume) times closeadj
def vlc_f089_volume_liquidity_context_log_126d_base_v008_signal(volume, closeadj):
    result = _mean(_volume_liquidity_context_log(volume), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(volume) times closeadj
def vlc_f089_volume_liquidity_context_log_252d_base_v009_signal(volume, closeadj):
    result = _mean(_volume_liquidity_context_log(volume), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(volume) times closeadj
def vlc_f089_volume_liquidity_context_log_504d_base_v010_signal(volume, closeadj):
    result = _mean(_volume_liquidity_context_log(volume), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume/close mean
def vlc_f089_volume_liquidity_context_per_close_63d_base_v011_signal(volume, close):
    result = _mean(_volume_liquidity_context_scaled(volume, close), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume/close mean
def vlc_f089_volume_liquidity_context_per_close_252d_base_v012_signal(volume, close):
    result = _mean(_volume_liquidity_context_scaled(volume, close), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume/close mean
def vlc_f089_volume_liquidity_context_per_close_504d_base_v013_signal(volume, close):
    result = _mean(_volume_liquidity_context_scaled(volume, close), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume/closeadj mean
def vlc_f089_volume_liquidity_context_per_closeadj_63d_base_v014_signal(volume, closeadj):
    result = _mean(_volume_liquidity_context_scaled(volume, closeadj), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume/closeadj mean
def vlc_f089_volume_liquidity_context_per_closeadj_252d_base_v015_signal(volume, closeadj):
    result = _mean(_volume_liquidity_context_scaled(volume, closeadj), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume/closeadj mean
def vlc_f089_volume_liquidity_context_per_closeadj_504d_base_v016_signal(volume, closeadj):
    result = _mean(_volume_liquidity_context_scaled(volume, closeadj), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume/sharesbas mean
def vlc_f089_volume_liquidity_context_per_sharesbas_63d_base_v017_signal(volume, sharesbas):
    result = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume/sharesbas mean
def vlc_f089_volume_liquidity_context_per_sharesbas_252d_base_v018_signal(volume, sharesbas):
    result = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume/sharesbas mean
def vlc_f089_volume_liquidity_context_per_sharesbas_504d_base_v019_signal(volume, sharesbas):
    result = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume/assets mean
def vlc_f089_volume_liquidity_context_per_assets_63d_base_v020_signal(volume, assets):
    result = _mean(_volume_liquidity_context_scaled(volume, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume/assets mean
def vlc_f089_volume_liquidity_context_per_assets_252d_base_v021_signal(volume, assets):
    result = _mean(_volume_liquidity_context_scaled(volume, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume/assets mean
def vlc_f089_volume_liquidity_context_per_assets_504d_base_v022_signal(volume, assets):
    result = _mean(_volume_liquidity_context_scaled(volume, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume/marketcap mean
def vlc_f089_volume_liquidity_context_per_marketcap_63d_base_v023_signal(volume, marketcap):
    result = _mean(_volume_liquidity_context_scaled(volume, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume/marketcap mean
def vlc_f089_volume_liquidity_context_per_marketcap_252d_base_v024_signal(volume, marketcap):
    result = _mean(_volume_liquidity_context_scaled(volume, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume/marketcap mean
def vlc_f089_volume_liquidity_context_per_marketcap_504d_base_v025_signal(volume, marketcap):
    result = _mean(_volume_liquidity_context_scaled(volume, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume per share times closeadj
def vlc_f089_volume_liquidity_context_pershare_21d_base_v026_signal(volume, sharesbas, closeadj):
    ps = _volume_liquidity_context_per_share(volume, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume per share times closeadj
def vlc_f089_volume_liquidity_context_pershare_63d_base_v027_signal(volume, sharesbas, closeadj):
    ps = _volume_liquidity_context_per_share(volume, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d volume per share times closeadj
def vlc_f089_volume_liquidity_context_pershare_126d_base_v028_signal(volume, sharesbas, closeadj):
    ps = _volume_liquidity_context_per_share(volume, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume per share times closeadj
def vlc_f089_volume_liquidity_context_pershare_252d_base_v029_signal(volume, sharesbas, closeadj):
    ps = _volume_liquidity_context_per_share(volume, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume per share times closeadj
def vlc_f089_volume_liquidity_context_pershare_504d_base_v030_signal(volume, sharesbas, closeadj):
    ps = _volume_liquidity_context_per_share(volume, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of volume times closeadj
def vlc_f089_volume_liquidity_context_std_63d_base_v031_signal(volume, closeadj):
    result = _std(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of volume times closeadj
def vlc_f089_volume_liquidity_context_std_252d_base_v032_signal(volume, closeadj):
    result = _std(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of volume times closeadj
def vlc_f089_volume_liquidity_context_std_504d_base_v033_signal(volume, closeadj):
    result = _std(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of volume
def vlc_f089_volume_liquidity_context_z_252d_base_v034_signal(volume):
    result = _z(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of volume
def vlc_f089_volume_liquidity_context_z_504d_base_v035_signal(volume):
    result = _z(volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(volume)
def vlc_f089_volume_liquidity_context_logz_252d_base_v036_signal(volume):
    result = _z(_volume_liquidity_context_log(volume), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(volume)
def vlc_f089_volume_liquidity_context_logz_504d_base_v037_signal(volume):
    result = _z(_volume_liquidity_context_log(volume), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of volume^2 times closeadj
def vlc_f089_volume_liquidity_context_sq_63d_base_v038_signal(volume, closeadj):
    result = _mean(volume * volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of volume^2 times closeadj
def vlc_f089_volume_liquidity_context_sq_252d_base_v039_signal(volume, closeadj):
    result = _mean(volume * volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(volume) times closeadj
def vlc_f089_volume_liquidity_context_sign_21d_base_v040_signal(volume, closeadj):
    result = _mean(np.sign(volume), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(volume) times closeadj
def vlc_f089_volume_liquidity_context_sign_63d_base_v041_signal(volume, closeadj):
    result = _mean(np.sign(volume), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(volume) times closeadj
def vlc_f089_volume_liquidity_context_sign_252d_base_v042_signal(volume, closeadj):
    result = _mean(np.sign(volume), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume/opex mean
def vlc_f089_volume_liquidity_context_per_opex_63d_base_v043_signal(volume, opex):
    result = _mean(_volume_liquidity_context_scaled(volume, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume/opex mean
def vlc_f089_volume_liquidity_context_per_opex_252d_base_v044_signal(volume, opex):
    result = _mean(_volume_liquidity_context_scaled(volume, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume/ebitda mean
def vlc_f089_volume_liquidity_context_per_ebitda_63d_base_v045_signal(volume, ebitda):
    result = _mean(_volume_liquidity_context_scaled(volume, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume/ebitda mean
def vlc_f089_volume_liquidity_context_per_ebitda_252d_base_v046_signal(volume, ebitda):
    result = _mean(_volume_liquidity_context_scaled(volume, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume/capex mean
def vlc_f089_volume_liquidity_context_per_capex_63d_base_v047_signal(volume, capex):
    result = _mean(_volume_liquidity_context_scaled(volume, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume/capex mean
def vlc_f089_volume_liquidity_context_per_capex_252d_base_v048_signal(volume, capex):
    result = _mean(_volume_liquidity_context_scaled(volume, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume/liabilities mean
def vlc_f089_volume_liquidity_context_per_liabilities_63d_base_v049_signal(volume, liabilities):
    result = _mean(_volume_liquidity_context_scaled(volume, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume/liabilities mean
def vlc_f089_volume_liquidity_context_per_liabilities_252d_base_v050_signal(volume, liabilities):
    result = _mean(_volume_liquidity_context_scaled(volume, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# volume relative to 252d max times closeadj
def vlc_f089_volume_liquidity_context_relmax_252d_base_v051_signal(volume, closeadj):
    peak = volume.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (volume / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# volume relative to 504d max times closeadj
def vlc_f089_volume_liquidity_context_relmax_504d_base_v052_signal(volume, closeadj):
    peak = volume.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (volume / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# volume relative to 252d min times closeadj
def vlc_f089_volume_liquidity_context_relmin_252d_base_v053_signal(volume, closeadj):
    trough = volume.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (volume / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# volume relative to 504d min times closeadj
def vlc_f089_volume_liquidity_context_relmin_504d_base_v054_signal(volume, closeadj):
    trough = volume.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (volume / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of volume times closeadj
def vlc_f089_volume_liquidity_context_pct_21d_base_v055_signal(volume, closeadj):
    result = _pct_change(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of volume times closeadj
def vlc_f089_volume_liquidity_context_pct_63d_base_v056_signal(volume, closeadj):
    result = _pct_change(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of volume times closeadj
def vlc_f089_volume_liquidity_context_pct_252d_base_v057_signal(volume, closeadj):
    result = _pct_change(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of volume times closeadj
def vlc_f089_volume_liquidity_context_sum_63d_base_v058_signal(volume, closeadj):
    result = volume.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of volume times closeadj
def vlc_f089_volume_liquidity_context_sum_252d_base_v059_signal(volume, closeadj):
    result = volume.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of volume times closeadj
def vlc_f089_volume_liquidity_context_sum_504d_base_v060_signal(volume, closeadj):
    result = volume.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed volume(63d) / smoothed close(252d) x closeadj
def vlc_f089_volume_liquidity_context_rom_close_252_63d_base_v061_signal(volume, close, closeadj):
    n = _mean(volume, 63)
    d = _mean(close, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed volume(126d) / smoothed close(504d) x closeadj
def vlc_f089_volume_liquidity_context_rom_close_504_126d_base_v062_signal(volume, close, closeadj):
    n = _mean(volume, 126)
    d = _mean(close, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed volume(63d) / smoothed closeadj(252d) x closeadj
def vlc_f089_volume_liquidity_context_rom_closeadj_252_63d_base_v063_signal(volume, closeadj):
    n = _mean(volume, 63)
    d = _mean(closeadj, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed volume(126d) / smoothed closeadj(504d) x closeadj
def vlc_f089_volume_liquidity_context_rom_closeadj_504_126d_base_v064_signal(volume, closeadj):
    n = _mean(volume, 126)
    d = _mean(closeadj, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed volume(63d) / smoothed sharesbas(252d) x closeadj
def vlc_f089_volume_liquidity_context_rom_sharesbas_252_63d_base_v065_signal(volume, sharesbas, closeadj):
    n = _mean(volume, 63)
    d = _mean(sharesbas, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed volume(126d) / smoothed sharesbas(504d) x closeadj
def vlc_f089_volume_liquidity_context_rom_sharesbas_504_126d_base_v066_signal(volume, sharesbas, closeadj):
    n = _mean(volume, 126)
    d = _mean(sharesbas, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(volume) / std(close)
def vlc_f089_volume_liquidity_context_volratio_close_252d_base_v067_signal(volume, close):
    n = _std(volume, 252)
    d = _std(close, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(volume) / std(close)
def vlc_f089_volume_liquidity_context_volratio_close_504d_base_v068_signal(volume, close):
    n = _std(volume, 504)
    d = _std(close, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(volume) / std(closeadj)
def vlc_f089_volume_liquidity_context_volratio_closeadj_252d_base_v069_signal(volume, closeadj):
    n = _std(volume, 252)
    d = _std(closeadj, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(volume) / std(closeadj)
def vlc_f089_volume_liquidity_context_volratio_closeadj_504d_base_v070_signal(volume, closeadj):
    n = _std(volume, 504)
    d = _std(closeadj, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed volume times closeadj
def vlc_f089_volume_liquidity_context_raw_5d_base_v071_signal(volume, closeadj):
    result = _mean(volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed volume times closeadj
def vlc_f089_volume_liquidity_context_raw_1008d_base_v072_signal(volume, closeadj):
    result = _mean(volume, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of volume/close
def vlc_f089_volume_liquidity_context_log_per_close_252d_base_v073_signal(volume, close):
    s = _volume_liquidity_context_scaled(volume, close)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of volume/close
def vlc_f089_volume_liquidity_context_log_per_close_504d_base_v074_signal(volume, close):
    s = _volume_liquidity_context_scaled(volume, close)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of volume/closeadj
def vlc_f089_volume_liquidity_context_log_per_closeadj_252d_base_v075_signal(volume, closeadj):
    s = _volume_liquidity_context_scaled(volume, closeadj)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
