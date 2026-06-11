"""Family f078 - TTM versus annual consistency (Fundamental Dynamics) | Sharadar tables: SF1 | fields: dimension, revenue, ncfo, netinc, rnd | base 001-075"""
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
def _ttm_vs_annual_consistency_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ttm_vs_annual_consistency_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ttm_vs_annual_consistency_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_raw_21d_base_v001_signal(dimension, closeadj):
    result = _mean(dimension, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_raw_63d_base_v002_signal(dimension, closeadj):
    result = _mean(dimension, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_raw_126d_base_v003_signal(dimension, closeadj):
    result = _mean(dimension, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_raw_252d_base_v004_signal(dimension, closeadj):
    result = _mean(dimension, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_raw_504d_base_v005_signal(dimension, closeadj):
    result = _mean(dimension, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(dimension) times closeadj
def tvac_f078_ttm_vs_annual_consistency_log_21d_base_v006_signal(dimension, closeadj):
    result = _mean(_ttm_vs_annual_consistency_log(dimension), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(dimension) times closeadj
def tvac_f078_ttm_vs_annual_consistency_log_63d_base_v007_signal(dimension, closeadj):
    result = _mean(_ttm_vs_annual_consistency_log(dimension), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(dimension) times closeadj
def tvac_f078_ttm_vs_annual_consistency_log_126d_base_v008_signal(dimension, closeadj):
    result = _mean(_ttm_vs_annual_consistency_log(dimension), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(dimension) times closeadj
def tvac_f078_ttm_vs_annual_consistency_log_252d_base_v009_signal(dimension, closeadj):
    result = _mean(_ttm_vs_annual_consistency_log(dimension), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(dimension) times closeadj
def tvac_f078_ttm_vs_annual_consistency_log_504d_base_v010_signal(dimension, closeadj):
    result = _mean(_ttm_vs_annual_consistency_log(dimension), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension/revenue mean
def tvac_f078_ttm_vs_annual_consistency_per_revenue_63d_base_v011_signal(dimension, revenue):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension/revenue mean
def tvac_f078_ttm_vs_annual_consistency_per_revenue_252d_base_v012_signal(dimension, revenue):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dimension/revenue mean
def tvac_f078_ttm_vs_annual_consistency_per_revenue_504d_base_v013_signal(dimension, revenue):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension/ncfo mean
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_63d_base_v014_signal(dimension, ncfo):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension/ncfo mean
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_252d_base_v015_signal(dimension, ncfo):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dimension/ncfo mean
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_504d_base_v016_signal(dimension, ncfo):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension/netinc mean
def tvac_f078_ttm_vs_annual_consistency_per_netinc_63d_base_v017_signal(dimension, netinc):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension/netinc mean
def tvac_f078_ttm_vs_annual_consistency_per_netinc_252d_base_v018_signal(dimension, netinc):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dimension/netinc mean
def tvac_f078_ttm_vs_annual_consistency_per_netinc_504d_base_v019_signal(dimension, netinc):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension/rnd mean
def tvac_f078_ttm_vs_annual_consistency_per_rnd_63d_base_v020_signal(dimension, rnd):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, rnd), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension/rnd mean
def tvac_f078_ttm_vs_annual_consistency_per_rnd_252d_base_v021_signal(dimension, rnd):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, rnd), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dimension/rnd mean
def tvac_f078_ttm_vs_annual_consistency_per_rnd_504d_base_v022_signal(dimension, rnd):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, rnd), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension/assets mean
def tvac_f078_ttm_vs_annual_consistency_per_assets_63d_base_v023_signal(dimension, assets):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension/assets mean
def tvac_f078_ttm_vs_annual_consistency_per_assets_252d_base_v024_signal(dimension, assets):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dimension/assets mean
def tvac_f078_ttm_vs_annual_consistency_per_assets_504d_base_v025_signal(dimension, assets):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dimension per share times closeadj
def tvac_f078_ttm_vs_annual_consistency_pershare_21d_base_v026_signal(dimension, sharesbas, closeadj):
    ps = _ttm_vs_annual_consistency_per_share(dimension, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension per share times closeadj
def tvac_f078_ttm_vs_annual_consistency_pershare_63d_base_v027_signal(dimension, sharesbas, closeadj):
    ps = _ttm_vs_annual_consistency_per_share(dimension, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dimension per share times closeadj
def tvac_f078_ttm_vs_annual_consistency_pershare_126d_base_v028_signal(dimension, sharesbas, closeadj):
    ps = _ttm_vs_annual_consistency_per_share(dimension, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension per share times closeadj
def tvac_f078_ttm_vs_annual_consistency_pershare_252d_base_v029_signal(dimension, sharesbas, closeadj):
    ps = _ttm_vs_annual_consistency_per_share(dimension, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dimension per share times closeadj
def tvac_f078_ttm_vs_annual_consistency_pershare_504d_base_v030_signal(dimension, sharesbas, closeadj):
    ps = _ttm_vs_annual_consistency_per_share(dimension, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_std_63d_base_v031_signal(dimension, closeadj):
    result = _std(dimension, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_std_252d_base_v032_signal(dimension, closeadj):
    result = _std(dimension, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_std_504d_base_v033_signal(dimension, closeadj):
    result = _std(dimension, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of dimension
def tvac_f078_ttm_vs_annual_consistency_z_252d_base_v034_signal(dimension):
    result = _z(dimension, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of dimension
def tvac_f078_ttm_vs_annual_consistency_z_504d_base_v035_signal(dimension):
    result = _z(dimension, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(dimension)
def tvac_f078_ttm_vs_annual_consistency_logz_252d_base_v036_signal(dimension):
    result = _z(_ttm_vs_annual_consistency_log(dimension), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(dimension)
def tvac_f078_ttm_vs_annual_consistency_logz_504d_base_v037_signal(dimension):
    result = _z(_ttm_vs_annual_consistency_log(dimension), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of dimension^2 times closeadj
def tvac_f078_ttm_vs_annual_consistency_sq_63d_base_v038_signal(dimension, closeadj):
    result = _mean(dimension * dimension, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of dimension^2 times closeadj
def tvac_f078_ttm_vs_annual_consistency_sq_252d_base_v039_signal(dimension, closeadj):
    result = _mean(dimension * dimension, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(dimension) times closeadj
def tvac_f078_ttm_vs_annual_consistency_sign_21d_base_v040_signal(dimension, closeadj):
    result = _mean(np.sign(dimension), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(dimension) times closeadj
def tvac_f078_ttm_vs_annual_consistency_sign_63d_base_v041_signal(dimension, closeadj):
    result = _mean(np.sign(dimension), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(dimension) times closeadj
def tvac_f078_ttm_vs_annual_consistency_sign_252d_base_v042_signal(dimension, closeadj):
    result = _mean(np.sign(dimension), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension/opex mean
def tvac_f078_ttm_vs_annual_consistency_per_opex_63d_base_v043_signal(dimension, opex):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension/opex mean
def tvac_f078_ttm_vs_annual_consistency_per_opex_252d_base_v044_signal(dimension, opex):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension/ebitda mean
def tvac_f078_ttm_vs_annual_consistency_per_ebitda_63d_base_v045_signal(dimension, ebitda):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension/ebitda mean
def tvac_f078_ttm_vs_annual_consistency_per_ebitda_252d_base_v046_signal(dimension, ebitda):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension/capex mean
def tvac_f078_ttm_vs_annual_consistency_per_capex_63d_base_v047_signal(dimension, capex):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension/capex mean
def tvac_f078_ttm_vs_annual_consistency_per_capex_252d_base_v048_signal(dimension, capex):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dimension/liabilities mean
def tvac_f078_ttm_vs_annual_consistency_per_liabilities_63d_base_v049_signal(dimension, liabilities):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dimension/liabilities mean
def tvac_f078_ttm_vs_annual_consistency_per_liabilities_252d_base_v050_signal(dimension, liabilities):
    result = _mean(_ttm_vs_annual_consistency_scaled(dimension, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dimension relative to 252d max times closeadj
def tvac_f078_ttm_vs_annual_consistency_relmax_252d_base_v051_signal(dimension, closeadj):
    peak = dimension.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (dimension / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dimension relative to 504d max times closeadj
def tvac_f078_ttm_vs_annual_consistency_relmax_504d_base_v052_signal(dimension, closeadj):
    peak = dimension.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (dimension / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dimension relative to 252d min times closeadj
def tvac_f078_ttm_vs_annual_consistency_relmin_252d_base_v053_signal(dimension, closeadj):
    trough = dimension.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (dimension / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dimension relative to 504d min times closeadj
def tvac_f078_ttm_vs_annual_consistency_relmin_504d_base_v054_signal(dimension, closeadj):
    trough = dimension.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (dimension / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_pct_21d_base_v055_signal(dimension, closeadj):
    result = _pct_change(dimension, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_pct_63d_base_v056_signal(dimension, closeadj):
    result = _pct_change(dimension, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_pct_252d_base_v057_signal(dimension, closeadj):
    result = _pct_change(dimension, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_sum_63d_base_v058_signal(dimension, closeadj):
    result = dimension.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_sum_252d_base_v059_signal(dimension, closeadj):
    result = dimension.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_sum_504d_base_v060_signal(dimension, closeadj):
    result = dimension.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dimension(63d) / smoothed revenue(252d) x closeadj
def tvac_f078_ttm_vs_annual_consistency_rom_revenue_252_63d_base_v061_signal(dimension, revenue, closeadj):
    n = _mean(dimension, 63)
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dimension(126d) / smoothed revenue(504d) x closeadj
def tvac_f078_ttm_vs_annual_consistency_rom_revenue_504_126d_base_v062_signal(dimension, revenue, closeadj):
    n = _mean(dimension, 126)
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dimension(63d) / smoothed ncfo(252d) x closeadj
def tvac_f078_ttm_vs_annual_consistency_rom_ncfo_252_63d_base_v063_signal(dimension, ncfo, closeadj):
    n = _mean(dimension, 63)
    d = _mean(ncfo, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dimension(126d) / smoothed ncfo(504d) x closeadj
def tvac_f078_ttm_vs_annual_consistency_rom_ncfo_504_126d_base_v064_signal(dimension, ncfo, closeadj):
    n = _mean(dimension, 126)
    d = _mean(ncfo, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dimension(63d) / smoothed netinc(252d) x closeadj
def tvac_f078_ttm_vs_annual_consistency_rom_netinc_252_63d_base_v065_signal(dimension, netinc, closeadj):
    n = _mean(dimension, 63)
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dimension(126d) / smoothed netinc(504d) x closeadj
def tvac_f078_ttm_vs_annual_consistency_rom_netinc_504_126d_base_v066_signal(dimension, netinc, closeadj):
    n = _mean(dimension, 126)
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(dimension) / std(revenue)
def tvac_f078_ttm_vs_annual_consistency_volratio_revenue_252d_base_v067_signal(dimension, revenue):
    n = _std(dimension, 252)
    d = _std(revenue, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(dimension) / std(revenue)
def tvac_f078_ttm_vs_annual_consistency_volratio_revenue_504d_base_v068_signal(dimension, revenue):
    n = _std(dimension, 504)
    d = _std(revenue, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(dimension) / std(ncfo)
def tvac_f078_ttm_vs_annual_consistency_volratio_ncfo_252d_base_v069_signal(dimension, ncfo):
    n = _std(dimension, 252)
    d = _std(ncfo, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(dimension) / std(ncfo)
def tvac_f078_ttm_vs_annual_consistency_volratio_ncfo_504d_base_v070_signal(dimension, ncfo):
    n = _std(dimension, 504)
    d = _std(ncfo, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_raw_5d_base_v071_signal(dimension, closeadj):
    result = _mean(dimension, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_raw_1008d_base_v072_signal(dimension, closeadj):
    result = _mean(dimension, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of dimension/revenue
def tvac_f078_ttm_vs_annual_consistency_log_per_revenue_252d_base_v073_signal(dimension, revenue):
    s = _ttm_vs_annual_consistency_scaled(dimension, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of dimension/revenue
def tvac_f078_ttm_vs_annual_consistency_log_per_revenue_504d_base_v074_signal(dimension, revenue):
    s = _ttm_vs_annual_consistency_scaled(dimension, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of dimension/ncfo
def tvac_f078_ttm_vs_annual_consistency_log_per_ncfo_252d_base_v075_signal(dimension, ncfo):
    s = _ttm_vs_annual_consistency_scaled(dimension, ncfo)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
