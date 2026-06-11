"""Family f16 - R&D intensity  (C_RnD_Innovation) | base 001-075"""
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
def _rnd_intensity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _rnd_intensity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _rnd_intensity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed rnd times closeadj
def ri_f16_rnd_intensity_raw_21d_base_v001_signal(rnd, closeadj):
    result = _mean(rnd, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed rnd times closeadj
def ri_f16_rnd_intensity_raw_63d_base_v002_signal(rnd, closeadj):
    result = _mean(rnd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed rnd times closeadj
def ri_f16_rnd_intensity_raw_126d_base_v003_signal(rnd, closeadj):
    result = _mean(rnd, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed rnd times closeadj
def ri_f16_rnd_intensity_raw_252d_base_v004_signal(rnd, closeadj):
    result = _mean(rnd, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed rnd times closeadj
def ri_f16_rnd_intensity_raw_504d_base_v005_signal(rnd, closeadj):
    result = _mean(rnd, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(rnd) times closeadj
def ri_f16_rnd_intensity_log_21d_base_v006_signal(rnd, closeadj):
    result = _mean(_rnd_intensity_log(rnd), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(rnd) times closeadj
def ri_f16_rnd_intensity_log_63d_base_v007_signal(rnd, closeadj):
    result = _mean(_rnd_intensity_log(rnd), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(rnd) times closeadj
def ri_f16_rnd_intensity_log_126d_base_v008_signal(rnd, closeadj):
    result = _mean(_rnd_intensity_log(rnd), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(rnd) times closeadj
def ri_f16_rnd_intensity_log_252d_base_v009_signal(rnd, closeadj):
    result = _mean(_rnd_intensity_log(rnd), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(rnd) times closeadj
def ri_f16_rnd_intensity_log_504d_base_v010_signal(rnd, closeadj):
    result = _mean(_rnd_intensity_log(rnd), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd/assets mean
def ri_f16_rnd_intensity_per_assets_63d_base_v011_signal(rnd, assets):
    result = _mean(_rnd_intensity_scaled(rnd, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd/assets mean
def ri_f16_rnd_intensity_per_assets_252d_base_v012_signal(rnd, assets):
    result = _mean(_rnd_intensity_scaled(rnd, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rnd/assets mean
def ri_f16_rnd_intensity_per_assets_504d_base_v013_signal(rnd, assets):
    result = _mean(_rnd_intensity_scaled(rnd, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd/marketcap mean
def ri_f16_rnd_intensity_per_marketcap_63d_base_v014_signal(rnd, marketcap):
    result = _mean(_rnd_intensity_scaled(rnd, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd/marketcap mean
def ri_f16_rnd_intensity_per_marketcap_252d_base_v015_signal(rnd, marketcap):
    result = _mean(_rnd_intensity_scaled(rnd, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rnd/marketcap mean
def ri_f16_rnd_intensity_per_marketcap_504d_base_v016_signal(rnd, marketcap):
    result = _mean(_rnd_intensity_scaled(rnd, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd/equity mean
def ri_f16_rnd_intensity_per_equity_63d_base_v017_signal(rnd, equity):
    result = _mean(_rnd_intensity_scaled(rnd, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd/equity mean
def ri_f16_rnd_intensity_per_equity_252d_base_v018_signal(rnd, equity):
    result = _mean(_rnd_intensity_scaled(rnd, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rnd/equity mean
def ri_f16_rnd_intensity_per_equity_504d_base_v019_signal(rnd, equity):
    result = _mean(_rnd_intensity_scaled(rnd, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd/debt mean
def ri_f16_rnd_intensity_per_debt_63d_base_v020_signal(rnd, debt):
    result = _mean(_rnd_intensity_scaled(rnd, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd/debt mean
def ri_f16_rnd_intensity_per_debt_252d_base_v021_signal(rnd, debt):
    result = _mean(_rnd_intensity_scaled(rnd, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rnd/debt mean
def ri_f16_rnd_intensity_per_debt_504d_base_v022_signal(rnd, debt):
    result = _mean(_rnd_intensity_scaled(rnd, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd/revenue mean
def ri_f16_rnd_intensity_per_revenue_63d_base_v023_signal(rnd, revenue):
    result = _mean(_rnd_intensity_scaled(rnd, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd/revenue mean
def ri_f16_rnd_intensity_per_revenue_252d_base_v024_signal(rnd, revenue):
    result = _mean(_rnd_intensity_scaled(rnd, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rnd/revenue mean
def ri_f16_rnd_intensity_per_revenue_504d_base_v025_signal(rnd, revenue):
    result = _mean(_rnd_intensity_scaled(rnd, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rnd per share times closeadj
def ri_f16_rnd_intensity_pershare_21d_base_v026_signal(rnd, sharesbas, closeadj):
    ps = _rnd_intensity_per_share(rnd, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd per share times closeadj
def ri_f16_rnd_intensity_pershare_63d_base_v027_signal(rnd, sharesbas, closeadj):
    ps = _rnd_intensity_per_share(rnd, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rnd per share times closeadj
def ri_f16_rnd_intensity_pershare_126d_base_v028_signal(rnd, sharesbas, closeadj):
    ps = _rnd_intensity_per_share(rnd, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd per share times closeadj
def ri_f16_rnd_intensity_pershare_252d_base_v029_signal(rnd, sharesbas, closeadj):
    ps = _rnd_intensity_per_share(rnd, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rnd per share times closeadj
def ri_f16_rnd_intensity_pershare_504d_base_v030_signal(rnd, sharesbas, closeadj):
    ps = _rnd_intensity_per_share(rnd, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of rnd times closeadj
def ri_f16_rnd_intensity_std_63d_base_v031_signal(rnd, closeadj):
    result = _std(rnd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of rnd times closeadj
def ri_f16_rnd_intensity_std_252d_base_v032_signal(rnd, closeadj):
    result = _std(rnd, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of rnd times closeadj
def ri_f16_rnd_intensity_std_504d_base_v033_signal(rnd, closeadj):
    result = _std(rnd, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of rnd
def ri_f16_rnd_intensity_z_252d_base_v034_signal(rnd):
    result = _z(rnd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of rnd
def ri_f16_rnd_intensity_z_504d_base_v035_signal(rnd):
    result = _z(rnd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(rnd)
def ri_f16_rnd_intensity_logz_252d_base_v036_signal(rnd):
    result = _z(_rnd_intensity_log(rnd), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(rnd)
def ri_f16_rnd_intensity_logz_504d_base_v037_signal(rnd):
    result = _z(_rnd_intensity_log(rnd), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of rnd^2 times closeadj
def ri_f16_rnd_intensity_sq_63d_base_v038_signal(rnd, closeadj):
    result = _mean(rnd * rnd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of rnd^2 times closeadj
def ri_f16_rnd_intensity_sq_252d_base_v039_signal(rnd, closeadj):
    result = _mean(rnd * rnd, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(rnd) times closeadj
def ri_f16_rnd_intensity_sign_21d_base_v040_signal(rnd, closeadj):
    result = _mean(np.sign(rnd), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(rnd) times closeadj
def ri_f16_rnd_intensity_sign_63d_base_v041_signal(rnd, closeadj):
    result = _mean(np.sign(rnd), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(rnd) times closeadj
def ri_f16_rnd_intensity_sign_252d_base_v042_signal(rnd, closeadj):
    result = _mean(np.sign(rnd), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd/opex mean
def ri_f16_rnd_intensity_per_opex_63d_base_v043_signal(rnd, opex):
    result = _mean(_rnd_intensity_scaled(rnd, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd/opex mean
def ri_f16_rnd_intensity_per_opex_252d_base_v044_signal(rnd, opex):
    result = _mean(_rnd_intensity_scaled(rnd, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd/ebitda mean
def ri_f16_rnd_intensity_per_ebitda_63d_base_v045_signal(rnd, ebitda):
    result = _mean(_rnd_intensity_scaled(rnd, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd/ebitda mean
def ri_f16_rnd_intensity_per_ebitda_252d_base_v046_signal(rnd, ebitda):
    result = _mean(_rnd_intensity_scaled(rnd, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd/capex mean
def ri_f16_rnd_intensity_per_capex_63d_base_v047_signal(rnd, capex):
    result = _mean(_rnd_intensity_scaled(rnd, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd/capex mean
def ri_f16_rnd_intensity_per_capex_252d_base_v048_signal(rnd, capex):
    result = _mean(_rnd_intensity_scaled(rnd, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rnd/liabilities mean
def ri_f16_rnd_intensity_per_liabilities_63d_base_v049_signal(rnd, liabilities):
    result = _mean(_rnd_intensity_scaled(rnd, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rnd/liabilities mean
def ri_f16_rnd_intensity_per_liabilities_252d_base_v050_signal(rnd, liabilities):
    result = _mean(_rnd_intensity_scaled(rnd, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rnd relative to 252d max times closeadj
def ri_f16_rnd_intensity_relmax_252d_base_v051_signal(rnd, closeadj):
    peak = rnd.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (rnd / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rnd relative to 504d max times closeadj
def ri_f16_rnd_intensity_relmax_504d_base_v052_signal(rnd, closeadj):
    peak = rnd.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (rnd / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rnd relative to 252d min times closeadj
def ri_f16_rnd_intensity_relmin_252d_base_v053_signal(rnd, closeadj):
    trough = rnd.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (rnd / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rnd relative to 504d min times closeadj
def ri_f16_rnd_intensity_relmin_504d_base_v054_signal(rnd, closeadj):
    trough = rnd.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (rnd / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of rnd times closeadj
def ri_f16_rnd_intensity_pct_21d_base_v055_signal(rnd, closeadj):
    result = _pct_change(rnd, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of rnd times closeadj
def ri_f16_rnd_intensity_pct_63d_base_v056_signal(rnd, closeadj):
    result = _pct_change(rnd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of rnd times closeadj
def ri_f16_rnd_intensity_pct_252d_base_v057_signal(rnd, closeadj):
    result = _pct_change(rnd, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of rnd times closeadj
def ri_f16_rnd_intensity_sum_63d_base_v058_signal(rnd, closeadj):
    result = rnd.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of rnd times closeadj
def ri_f16_rnd_intensity_sum_252d_base_v059_signal(rnd, closeadj):
    result = rnd.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of rnd times closeadj
def ri_f16_rnd_intensity_sum_504d_base_v060_signal(rnd, closeadj):
    result = rnd.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed rnd(63d) / smoothed assets(252d) x closeadj
def ri_f16_rnd_intensity_rom_assets_252_63d_base_v061_signal(rnd, assets, closeadj):
    n = _mean(rnd, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed rnd(126d) / smoothed assets(504d) x closeadj
def ri_f16_rnd_intensity_rom_assets_504_126d_base_v062_signal(rnd, assets, closeadj):
    n = _mean(rnd, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed rnd(63d) / smoothed marketcap(252d) x closeadj
def ri_f16_rnd_intensity_rom_marketcap_252_63d_base_v063_signal(rnd, marketcap, closeadj):
    n = _mean(rnd, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed rnd(126d) / smoothed marketcap(504d) x closeadj
def ri_f16_rnd_intensity_rom_marketcap_504_126d_base_v064_signal(rnd, marketcap, closeadj):
    n = _mean(rnd, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed rnd(63d) / smoothed equity(252d) x closeadj
def ri_f16_rnd_intensity_rom_equity_252_63d_base_v065_signal(rnd, equity, closeadj):
    n = _mean(rnd, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed rnd(126d) / smoothed equity(504d) x closeadj
def ri_f16_rnd_intensity_rom_equity_504_126d_base_v066_signal(rnd, equity, closeadj):
    n = _mean(rnd, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(rnd) / std(assets)
def ri_f16_rnd_intensity_volratio_assets_252d_base_v067_signal(rnd, assets):
    n = _std(rnd, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(rnd) / std(assets)
def ri_f16_rnd_intensity_volratio_assets_504d_base_v068_signal(rnd, assets):
    n = _std(rnd, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(rnd) / std(marketcap)
def ri_f16_rnd_intensity_volratio_marketcap_252d_base_v069_signal(rnd, marketcap):
    n = _std(rnd, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(rnd) / std(marketcap)
def ri_f16_rnd_intensity_volratio_marketcap_504d_base_v070_signal(rnd, marketcap):
    n = _std(rnd, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed rnd times closeadj
def ri_f16_rnd_intensity_raw_5d_base_v071_signal(rnd, closeadj):
    result = _mean(rnd, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed rnd times closeadj
def ri_f16_rnd_intensity_raw_1008d_base_v072_signal(rnd, closeadj):
    result = _mean(rnd, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of rnd/assets
def ri_f16_rnd_intensity_log_per_assets_252d_base_v073_signal(rnd, assets):
    s = _rnd_intensity_scaled(rnd, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of rnd/assets
def ri_f16_rnd_intensity_log_per_assets_504d_base_v074_signal(rnd, assets):
    s = _rnd_intensity_scaled(rnd, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of rnd/marketcap
def ri_f16_rnd_intensity_log_per_marketcap_252d_base_v075_signal(rnd, marketcap):
    s = _rnd_intensity_scaled(rnd, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
