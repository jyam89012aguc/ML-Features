"""Family f090 - Adjusted versus unadjusted price integrity (Market Context from Sharadar Prices) | Sharadar tables: SEP,SFP | fields: close, closeadj, closeunadj, open, high, low | base 001-075"""
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
def _price_adjustment_context_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _price_adjustment_context_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _price_adjustment_context_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed close times closeadj
def pac_f090_price_adjustment_context_raw_21d_base_v001_signal(close, closeadj):
    result = _mean(close, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed close times closeadj
def pac_f090_price_adjustment_context_raw_63d_base_v002_signal(close, closeadj):
    result = _mean(close, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed close times closeadj
def pac_f090_price_adjustment_context_raw_126d_base_v003_signal(close, closeadj):
    result = _mean(close, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed close times closeadj
def pac_f090_price_adjustment_context_raw_252d_base_v004_signal(close, closeadj):
    result = _mean(close, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed close times closeadj
def pac_f090_price_adjustment_context_raw_504d_base_v005_signal(close, closeadj):
    result = _mean(close, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(close) times closeadj
def pac_f090_price_adjustment_context_log_21d_base_v006_signal(close, closeadj):
    result = _mean(_price_adjustment_context_log(close), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(close) times closeadj
def pac_f090_price_adjustment_context_log_63d_base_v007_signal(close, closeadj):
    result = _mean(_price_adjustment_context_log(close), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(close) times closeadj
def pac_f090_price_adjustment_context_log_126d_base_v008_signal(close, closeadj):
    result = _mean(_price_adjustment_context_log(close), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(close) times closeadj
def pac_f090_price_adjustment_context_log_252d_base_v009_signal(close, closeadj):
    result = _mean(_price_adjustment_context_log(close), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(close) times closeadj
def pac_f090_price_adjustment_context_log_504d_base_v010_signal(close, closeadj):
    result = _mean(_price_adjustment_context_log(close), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close/closeadj mean
def pac_f090_price_adjustment_context_per_closeadj_63d_base_v011_signal(close, closeadj):
    result = _mean(_price_adjustment_context_scaled(close, closeadj), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close/closeadj mean
def pac_f090_price_adjustment_context_per_closeadj_252d_base_v012_signal(close, closeadj):
    result = _mean(_price_adjustment_context_scaled(close, closeadj), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d close/closeadj mean
def pac_f090_price_adjustment_context_per_closeadj_504d_base_v013_signal(close, closeadj):
    result = _mean(_price_adjustment_context_scaled(close, closeadj), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close/closeunadj mean
def pac_f090_price_adjustment_context_per_closeunadj_63d_base_v014_signal(close, closeunadj):
    result = _mean(_price_adjustment_context_scaled(close, closeunadj), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close/closeunadj mean
def pac_f090_price_adjustment_context_per_closeunadj_252d_base_v015_signal(close, closeunadj):
    result = _mean(_price_adjustment_context_scaled(close, closeunadj), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d close/closeunadj mean
def pac_f090_price_adjustment_context_per_closeunadj_504d_base_v016_signal(close, closeunadj):
    result = _mean(_price_adjustment_context_scaled(close, closeunadj), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close/open mean
def pac_f090_price_adjustment_context_per_open_63d_base_v017_signal(close, open):
    result = _mean(_price_adjustment_context_scaled(close, open), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close/open mean
def pac_f090_price_adjustment_context_per_open_252d_base_v018_signal(close, open):
    result = _mean(_price_adjustment_context_scaled(close, open), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d close/open mean
def pac_f090_price_adjustment_context_per_open_504d_base_v019_signal(close, open):
    result = _mean(_price_adjustment_context_scaled(close, open), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close/high mean
def pac_f090_price_adjustment_context_per_high_63d_base_v020_signal(close, high):
    result = _mean(_price_adjustment_context_scaled(close, high), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close/high mean
def pac_f090_price_adjustment_context_per_high_252d_base_v021_signal(close, high):
    result = _mean(_price_adjustment_context_scaled(close, high), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d close/high mean
def pac_f090_price_adjustment_context_per_high_504d_base_v022_signal(close, high):
    result = _mean(_price_adjustment_context_scaled(close, high), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close/low mean
def pac_f090_price_adjustment_context_per_low_63d_base_v023_signal(close, low):
    result = _mean(_price_adjustment_context_scaled(close, low), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close/low mean
def pac_f090_price_adjustment_context_per_low_252d_base_v024_signal(close, low):
    result = _mean(_price_adjustment_context_scaled(close, low), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d close/low mean
def pac_f090_price_adjustment_context_per_low_504d_base_v025_signal(close, low):
    result = _mean(_price_adjustment_context_scaled(close, low), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d close per share times closeadj
def pac_f090_price_adjustment_context_pershare_21d_base_v026_signal(close, sharesbas, closeadj):
    ps = _price_adjustment_context_per_share(close, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close per share times closeadj
def pac_f090_price_adjustment_context_pershare_63d_base_v027_signal(close, sharesbas, closeadj):
    ps = _price_adjustment_context_per_share(close, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d close per share times closeadj
def pac_f090_price_adjustment_context_pershare_126d_base_v028_signal(close, sharesbas, closeadj):
    ps = _price_adjustment_context_per_share(close, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close per share times closeadj
def pac_f090_price_adjustment_context_pershare_252d_base_v029_signal(close, sharesbas, closeadj):
    ps = _price_adjustment_context_per_share(close, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d close per share times closeadj
def pac_f090_price_adjustment_context_pershare_504d_base_v030_signal(close, sharesbas, closeadj):
    ps = _price_adjustment_context_per_share(close, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of close times closeadj
def pac_f090_price_adjustment_context_std_63d_base_v031_signal(close, closeadj):
    result = _std(close, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of close times closeadj
def pac_f090_price_adjustment_context_std_252d_base_v032_signal(close, closeadj):
    result = _std(close, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of close times closeadj
def pac_f090_price_adjustment_context_std_504d_base_v033_signal(close, closeadj):
    result = _std(close, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of close
def pac_f090_price_adjustment_context_z_252d_base_v034_signal(close):
    result = _z(close, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of close
def pac_f090_price_adjustment_context_z_504d_base_v035_signal(close):
    result = _z(close, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(close)
def pac_f090_price_adjustment_context_logz_252d_base_v036_signal(close):
    result = _z(_price_adjustment_context_log(close), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(close)
def pac_f090_price_adjustment_context_logz_504d_base_v037_signal(close):
    result = _z(_price_adjustment_context_log(close), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of close^2 times closeadj
def pac_f090_price_adjustment_context_sq_63d_base_v038_signal(close, closeadj):
    result = _mean(close * close, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of close^2 times closeadj
def pac_f090_price_adjustment_context_sq_252d_base_v039_signal(close, closeadj):
    result = _mean(close * close, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(close) times closeadj
def pac_f090_price_adjustment_context_sign_21d_base_v040_signal(close, closeadj):
    result = _mean(np.sign(close), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(close) times closeadj
def pac_f090_price_adjustment_context_sign_63d_base_v041_signal(close, closeadj):
    result = _mean(np.sign(close), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(close) times closeadj
def pac_f090_price_adjustment_context_sign_252d_base_v042_signal(close, closeadj):
    result = _mean(np.sign(close), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close/opex mean
def pac_f090_price_adjustment_context_per_opex_63d_base_v043_signal(close, opex):
    result = _mean(_price_adjustment_context_scaled(close, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close/opex mean
def pac_f090_price_adjustment_context_per_opex_252d_base_v044_signal(close, opex):
    result = _mean(_price_adjustment_context_scaled(close, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close/ebitda mean
def pac_f090_price_adjustment_context_per_ebitda_63d_base_v045_signal(close, ebitda):
    result = _mean(_price_adjustment_context_scaled(close, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close/ebitda mean
def pac_f090_price_adjustment_context_per_ebitda_252d_base_v046_signal(close, ebitda):
    result = _mean(_price_adjustment_context_scaled(close, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close/capex mean
def pac_f090_price_adjustment_context_per_capex_63d_base_v047_signal(close, capex):
    result = _mean(_price_adjustment_context_scaled(close, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close/capex mean
def pac_f090_price_adjustment_context_per_capex_252d_base_v048_signal(close, capex):
    result = _mean(_price_adjustment_context_scaled(close, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close/liabilities mean
def pac_f090_price_adjustment_context_per_liabilities_63d_base_v049_signal(close, liabilities):
    result = _mean(_price_adjustment_context_scaled(close, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close/liabilities mean
def pac_f090_price_adjustment_context_per_liabilities_252d_base_v050_signal(close, liabilities):
    result = _mean(_price_adjustment_context_scaled(close, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# close relative to 252d max times closeadj
def pac_f090_price_adjustment_context_relmax_252d_base_v051_signal(close, closeadj):
    peak = close.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (close / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# close relative to 504d max times closeadj
def pac_f090_price_adjustment_context_relmax_504d_base_v052_signal(close, closeadj):
    peak = close.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (close / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# close relative to 252d min times closeadj
def pac_f090_price_adjustment_context_relmin_252d_base_v053_signal(close, closeadj):
    trough = close.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (close / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# close relative to 504d min times closeadj
def pac_f090_price_adjustment_context_relmin_504d_base_v054_signal(close, closeadj):
    trough = close.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (close / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of close times closeadj
def pac_f090_price_adjustment_context_pct_21d_base_v055_signal(close, closeadj):
    result = _pct_change(close, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of close times closeadj
def pac_f090_price_adjustment_context_pct_63d_base_v056_signal(close, closeadj):
    result = _pct_change(close, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of close times closeadj
def pac_f090_price_adjustment_context_pct_252d_base_v057_signal(close, closeadj):
    result = _pct_change(close, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of close times closeadj
def pac_f090_price_adjustment_context_sum_63d_base_v058_signal(close, closeadj):
    result = close.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of close times closeadj
def pac_f090_price_adjustment_context_sum_252d_base_v059_signal(close, closeadj):
    result = close.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of close times closeadj
def pac_f090_price_adjustment_context_sum_504d_base_v060_signal(close, closeadj):
    result = close.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed close(63d) / smoothed closeadj(252d) x closeadj
def pac_f090_price_adjustment_context_rom_closeadj_252_63d_base_v061_signal(close, closeadj):
    n = _mean(close, 63)
    d = _mean(closeadj, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed close(126d) / smoothed closeadj(504d) x closeadj
def pac_f090_price_adjustment_context_rom_closeadj_504_126d_base_v062_signal(close, closeadj):
    n = _mean(close, 126)
    d = _mean(closeadj, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed close(63d) / smoothed closeunadj(252d) x closeadj
def pac_f090_price_adjustment_context_rom_closeunadj_252_63d_base_v063_signal(close, closeunadj, closeadj):
    n = _mean(close, 63)
    d = _mean(closeunadj, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed close(126d) / smoothed closeunadj(504d) x closeadj
def pac_f090_price_adjustment_context_rom_closeunadj_504_126d_base_v064_signal(close, closeunadj, closeadj):
    n = _mean(close, 126)
    d = _mean(closeunadj, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed close(63d) / smoothed open(252d) x closeadj
def pac_f090_price_adjustment_context_rom_open_252_63d_base_v065_signal(close, open, closeadj):
    n = _mean(close, 63)
    d = _mean(open, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed close(126d) / smoothed open(504d) x closeadj
def pac_f090_price_adjustment_context_rom_open_504_126d_base_v066_signal(close, open, closeadj):
    n = _mean(close, 126)
    d = _mean(open, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(close) / std(closeadj)
def pac_f090_price_adjustment_context_volratio_closeadj_252d_base_v067_signal(close, closeadj):
    n = _std(close, 252)
    d = _std(closeadj, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(close) / std(closeadj)
def pac_f090_price_adjustment_context_volratio_closeadj_504d_base_v068_signal(close, closeadj):
    n = _std(close, 504)
    d = _std(closeadj, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(close) / std(closeunadj)
def pac_f090_price_adjustment_context_volratio_closeunadj_252d_base_v069_signal(close, closeunadj):
    n = _std(close, 252)
    d = _std(closeunadj, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(close) / std(closeunadj)
def pac_f090_price_adjustment_context_volratio_closeunadj_504d_base_v070_signal(close, closeunadj):
    n = _std(close, 504)
    d = _std(closeunadj, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed close times closeadj
def pac_f090_price_adjustment_context_raw_5d_base_v071_signal(close, closeadj):
    result = _mean(close, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed close times closeadj
def pac_f090_price_adjustment_context_raw_1008d_base_v072_signal(close, closeadj):
    result = _mean(close, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of close/closeadj
def pac_f090_price_adjustment_context_log_per_closeadj_252d_base_v073_signal(close, closeadj):
    s = _price_adjustment_context_scaled(close, closeadj)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of close/closeadj
def pac_f090_price_adjustment_context_log_per_closeadj_504d_base_v074_signal(close, closeadj):
    s = _price_adjustment_context_scaled(close, closeadj)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of close/closeunadj
def pac_f090_price_adjustment_context_log_per_closeunadj_252d_base_v075_signal(close, closeunadj):
    s = _price_adjustment_context_scaled(close, closeunadj)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
