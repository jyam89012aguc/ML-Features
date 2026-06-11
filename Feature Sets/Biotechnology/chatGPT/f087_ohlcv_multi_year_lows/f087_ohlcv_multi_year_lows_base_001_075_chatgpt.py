"""Family f087 - OHLCV lowest-lows context (Market Context from Sharadar Prices) | Sharadar tables: SEP,SFP | fields: date, open, high, low, close, volume, closeadj, closeunadj | base 001-075"""
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
def _ohlcv_multi_year_lows_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ohlcv_multi_year_lows_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ohlcv_multi_year_lows_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed open times closeadj
def omyl_f087_ohlcv_multi_year_lows_raw_21d_base_v001_signal(open, closeadj):
    result = _mean(open, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed open times closeadj
def omyl_f087_ohlcv_multi_year_lows_raw_63d_base_v002_signal(open, closeadj):
    result = _mean(open, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed open times closeadj
def omyl_f087_ohlcv_multi_year_lows_raw_126d_base_v003_signal(open, closeadj):
    result = _mean(open, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed open times closeadj
def omyl_f087_ohlcv_multi_year_lows_raw_252d_base_v004_signal(open, closeadj):
    result = _mean(open, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed open times closeadj
def omyl_f087_ohlcv_multi_year_lows_raw_504d_base_v005_signal(open, closeadj):
    result = _mean(open, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(open) times closeadj
def omyl_f087_ohlcv_multi_year_lows_log_21d_base_v006_signal(open, closeadj):
    result = _mean(_ohlcv_multi_year_lows_log(open), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(open) times closeadj
def omyl_f087_ohlcv_multi_year_lows_log_63d_base_v007_signal(open, closeadj):
    result = _mean(_ohlcv_multi_year_lows_log(open), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(open) times closeadj
def omyl_f087_ohlcv_multi_year_lows_log_126d_base_v008_signal(open, closeadj):
    result = _mean(_ohlcv_multi_year_lows_log(open), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(open) times closeadj
def omyl_f087_ohlcv_multi_year_lows_log_252d_base_v009_signal(open, closeadj):
    result = _mean(_ohlcv_multi_year_lows_log(open), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(open) times closeadj
def omyl_f087_ohlcv_multi_year_lows_log_504d_base_v010_signal(open, closeadj):
    result = _mean(_ohlcv_multi_year_lows_log(open), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open/high mean
def omyl_f087_ohlcv_multi_year_lows_per_high_63d_base_v011_signal(open, high):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, high), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open/high mean
def omyl_f087_ohlcv_multi_year_lows_per_high_252d_base_v012_signal(open, high):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, high), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d open/high mean
def omyl_f087_ohlcv_multi_year_lows_per_high_504d_base_v013_signal(open, high):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, high), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open/low mean
def omyl_f087_ohlcv_multi_year_lows_per_low_63d_base_v014_signal(open, low):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, low), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open/low mean
def omyl_f087_ohlcv_multi_year_lows_per_low_252d_base_v015_signal(open, low):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, low), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d open/low mean
def omyl_f087_ohlcv_multi_year_lows_per_low_504d_base_v016_signal(open, low):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, low), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open/close mean
def omyl_f087_ohlcv_multi_year_lows_per_close_63d_base_v017_signal(open, close):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, close), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open/close mean
def omyl_f087_ohlcv_multi_year_lows_per_close_252d_base_v018_signal(open, close):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, close), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d open/close mean
def omyl_f087_ohlcv_multi_year_lows_per_close_504d_base_v019_signal(open, close):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, close), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open/volume mean
def omyl_f087_ohlcv_multi_year_lows_per_volume_63d_base_v020_signal(open, volume):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, volume), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open/volume mean
def omyl_f087_ohlcv_multi_year_lows_per_volume_252d_base_v021_signal(open, volume):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, volume), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d open/volume mean
def omyl_f087_ohlcv_multi_year_lows_per_volume_504d_base_v022_signal(open, volume):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, volume), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open/closeadj mean
def omyl_f087_ohlcv_multi_year_lows_per_closeadj_63d_base_v023_signal(open, closeadj):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, closeadj), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open/closeadj mean
def omyl_f087_ohlcv_multi_year_lows_per_closeadj_252d_base_v024_signal(open, closeadj):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, closeadj), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d open/closeadj mean
def omyl_f087_ohlcv_multi_year_lows_per_closeadj_504d_base_v025_signal(open, closeadj):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, closeadj), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d open per share times closeadj
def omyl_f087_ohlcv_multi_year_lows_pershare_21d_base_v026_signal(open, sharesbas, closeadj):
    ps = _ohlcv_multi_year_lows_per_share(open, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open per share times closeadj
def omyl_f087_ohlcv_multi_year_lows_pershare_63d_base_v027_signal(open, sharesbas, closeadj):
    ps = _ohlcv_multi_year_lows_per_share(open, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d open per share times closeadj
def omyl_f087_ohlcv_multi_year_lows_pershare_126d_base_v028_signal(open, sharesbas, closeadj):
    ps = _ohlcv_multi_year_lows_per_share(open, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open per share times closeadj
def omyl_f087_ohlcv_multi_year_lows_pershare_252d_base_v029_signal(open, sharesbas, closeadj):
    ps = _ohlcv_multi_year_lows_per_share(open, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d open per share times closeadj
def omyl_f087_ohlcv_multi_year_lows_pershare_504d_base_v030_signal(open, sharesbas, closeadj):
    ps = _ohlcv_multi_year_lows_per_share(open, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of open times closeadj
def omyl_f087_ohlcv_multi_year_lows_std_63d_base_v031_signal(open, closeadj):
    result = _std(open, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of open times closeadj
def omyl_f087_ohlcv_multi_year_lows_std_252d_base_v032_signal(open, closeadj):
    result = _std(open, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of open times closeadj
def omyl_f087_ohlcv_multi_year_lows_std_504d_base_v033_signal(open, closeadj):
    result = _std(open, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of open
def omyl_f087_ohlcv_multi_year_lows_z_252d_base_v034_signal(open):
    result = _z(open, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of open
def omyl_f087_ohlcv_multi_year_lows_z_504d_base_v035_signal(open):
    result = _z(open, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(open)
def omyl_f087_ohlcv_multi_year_lows_logz_252d_base_v036_signal(open):
    result = _z(_ohlcv_multi_year_lows_log(open), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(open)
def omyl_f087_ohlcv_multi_year_lows_logz_504d_base_v037_signal(open):
    result = _z(_ohlcv_multi_year_lows_log(open), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of open^2 times closeadj
def omyl_f087_ohlcv_multi_year_lows_sq_63d_base_v038_signal(open, closeadj):
    result = _mean(open * open, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of open^2 times closeadj
def omyl_f087_ohlcv_multi_year_lows_sq_252d_base_v039_signal(open, closeadj):
    result = _mean(open * open, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(open) times closeadj
def omyl_f087_ohlcv_multi_year_lows_sign_21d_base_v040_signal(open, closeadj):
    result = _mean(np.sign(open), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(open) times closeadj
def omyl_f087_ohlcv_multi_year_lows_sign_63d_base_v041_signal(open, closeadj):
    result = _mean(np.sign(open), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(open) times closeadj
def omyl_f087_ohlcv_multi_year_lows_sign_252d_base_v042_signal(open, closeadj):
    result = _mean(np.sign(open), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open/opex mean
def omyl_f087_ohlcv_multi_year_lows_per_opex_63d_base_v043_signal(open, opex):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open/opex mean
def omyl_f087_ohlcv_multi_year_lows_per_opex_252d_base_v044_signal(open, opex):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open/ebitda mean
def omyl_f087_ohlcv_multi_year_lows_per_ebitda_63d_base_v045_signal(open, ebitda):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open/ebitda mean
def omyl_f087_ohlcv_multi_year_lows_per_ebitda_252d_base_v046_signal(open, ebitda):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open/capex mean
def omyl_f087_ohlcv_multi_year_lows_per_capex_63d_base_v047_signal(open, capex):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open/capex mean
def omyl_f087_ohlcv_multi_year_lows_per_capex_252d_base_v048_signal(open, capex):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d open/liabilities mean
def omyl_f087_ohlcv_multi_year_lows_per_liabilities_63d_base_v049_signal(open, liabilities):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d open/liabilities mean
def omyl_f087_ohlcv_multi_year_lows_per_liabilities_252d_base_v050_signal(open, liabilities):
    result = _mean(_ohlcv_multi_year_lows_scaled(open, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# open relative to 252d max times closeadj
def omyl_f087_ohlcv_multi_year_lows_relmax_252d_base_v051_signal(open, closeadj):
    peak = open.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (open / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# open relative to 504d max times closeadj
def omyl_f087_ohlcv_multi_year_lows_relmax_504d_base_v052_signal(open, closeadj):
    peak = open.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (open / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# open relative to 252d min times closeadj
def omyl_f087_ohlcv_multi_year_lows_relmin_252d_base_v053_signal(open, closeadj):
    trough = open.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (open / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# open relative to 504d min times closeadj
def omyl_f087_ohlcv_multi_year_lows_relmin_504d_base_v054_signal(open, closeadj):
    trough = open.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (open / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of open times closeadj
def omyl_f087_ohlcv_multi_year_lows_pct_21d_base_v055_signal(open, closeadj):
    result = _pct_change(open, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of open times closeadj
def omyl_f087_ohlcv_multi_year_lows_pct_63d_base_v056_signal(open, closeadj):
    result = _pct_change(open, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of open times closeadj
def omyl_f087_ohlcv_multi_year_lows_pct_252d_base_v057_signal(open, closeadj):
    result = _pct_change(open, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of open times closeadj
def omyl_f087_ohlcv_multi_year_lows_sum_63d_base_v058_signal(open, closeadj):
    result = open.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of open times closeadj
def omyl_f087_ohlcv_multi_year_lows_sum_252d_base_v059_signal(open, closeadj):
    result = open.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of open times closeadj
def omyl_f087_ohlcv_multi_year_lows_sum_504d_base_v060_signal(open, closeadj):
    result = open.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed open(63d) / smoothed high(252d) x closeadj
def omyl_f087_ohlcv_multi_year_lows_rom_high_252_63d_base_v061_signal(open, high, closeadj):
    n = _mean(open, 63)
    d = _mean(high, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed open(126d) / smoothed high(504d) x closeadj
def omyl_f087_ohlcv_multi_year_lows_rom_high_504_126d_base_v062_signal(open, high, closeadj):
    n = _mean(open, 126)
    d = _mean(high, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed open(63d) / smoothed low(252d) x closeadj
def omyl_f087_ohlcv_multi_year_lows_rom_low_252_63d_base_v063_signal(open, low, closeadj):
    n = _mean(open, 63)
    d = _mean(low, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed open(126d) / smoothed low(504d) x closeadj
def omyl_f087_ohlcv_multi_year_lows_rom_low_504_126d_base_v064_signal(open, low, closeadj):
    n = _mean(open, 126)
    d = _mean(low, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed open(63d) / smoothed close(252d) x closeadj
def omyl_f087_ohlcv_multi_year_lows_rom_close_252_63d_base_v065_signal(open, close, closeadj):
    n = _mean(open, 63)
    d = _mean(close, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed open(126d) / smoothed close(504d) x closeadj
def omyl_f087_ohlcv_multi_year_lows_rom_close_504_126d_base_v066_signal(open, close, closeadj):
    n = _mean(open, 126)
    d = _mean(close, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(open) / std(high)
def omyl_f087_ohlcv_multi_year_lows_volratio_high_252d_base_v067_signal(open, high):
    n = _std(open, 252)
    d = _std(high, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(open) / std(high)
def omyl_f087_ohlcv_multi_year_lows_volratio_high_504d_base_v068_signal(open, high):
    n = _std(open, 504)
    d = _std(high, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(open) / std(low)
def omyl_f087_ohlcv_multi_year_lows_volratio_low_252d_base_v069_signal(open, low):
    n = _std(open, 252)
    d = _std(low, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(open) / std(low)
def omyl_f087_ohlcv_multi_year_lows_volratio_low_504d_base_v070_signal(open, low):
    n = _std(open, 504)
    d = _std(low, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed open times closeadj
def omyl_f087_ohlcv_multi_year_lows_raw_5d_base_v071_signal(open, closeadj):
    result = _mean(open, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed open times closeadj
def omyl_f087_ohlcv_multi_year_lows_raw_1008d_base_v072_signal(open, closeadj):
    result = _mean(open, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of open/high
def omyl_f087_ohlcv_multi_year_lows_log_per_high_252d_base_v073_signal(open, high):
    s = _ohlcv_multi_year_lows_scaled(open, high)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of open/high
def omyl_f087_ohlcv_multi_year_lows_log_per_high_504d_base_v074_signal(open, high):
    s = _ohlcv_multi_year_lows_scaled(open, high)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of open/low
def omyl_f087_ohlcv_multi_year_lows_log_per_low_252d_base_v075_signal(open, low):
    s = _ohlcv_multi_year_lows_scaled(open, low)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
