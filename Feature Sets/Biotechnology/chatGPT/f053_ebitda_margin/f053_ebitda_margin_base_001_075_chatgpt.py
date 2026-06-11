"""Family f053 - EBITDA profitability (Margins and Profitability) | Sharadar tables: SF1 | fields: ebitda, ebitdamargin, revenue | base 001-075"""
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
def _ebitda_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ebitda_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ebitda_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed ebitda times closeadj
def em_f053_ebitda_margin_raw_21d_base_v001_signal(ebitda, closeadj):
    result = _mean(ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed ebitda times closeadj
def em_f053_ebitda_margin_raw_63d_base_v002_signal(ebitda, closeadj):
    result = _mean(ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed ebitda times closeadj
def em_f053_ebitda_margin_raw_126d_base_v003_signal(ebitda, closeadj):
    result = _mean(ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed ebitda times closeadj
def em_f053_ebitda_margin_raw_252d_base_v004_signal(ebitda, closeadj):
    result = _mean(ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed ebitda times closeadj
def em_f053_ebitda_margin_raw_504d_base_v005_signal(ebitda, closeadj):
    result = _mean(ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(ebitda) times closeadj
def em_f053_ebitda_margin_log_21d_base_v006_signal(ebitda, closeadj):
    result = _mean(_ebitda_margin_log(ebitda), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(ebitda) times closeadj
def em_f053_ebitda_margin_log_63d_base_v007_signal(ebitda, closeadj):
    result = _mean(_ebitda_margin_log(ebitda), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(ebitda) times closeadj
def em_f053_ebitda_margin_log_126d_base_v008_signal(ebitda, closeadj):
    result = _mean(_ebitda_margin_log(ebitda), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(ebitda) times closeadj
def em_f053_ebitda_margin_log_252d_base_v009_signal(ebitda, closeadj):
    result = _mean(_ebitda_margin_log(ebitda), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(ebitda) times closeadj
def em_f053_ebitda_margin_log_504d_base_v010_signal(ebitda, closeadj):
    result = _mean(_ebitda_margin_log(ebitda), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda/ebitdamargin mean
def em_f053_ebitda_margin_per_ebitdamargin_63d_base_v011_signal(ebitda, ebitdamargin):
    result = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/ebitdamargin mean
def em_f053_ebitda_margin_per_ebitdamargin_252d_base_v012_signal(ebitda, ebitdamargin):
    result = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda/ebitdamargin mean
def em_f053_ebitda_margin_per_ebitdamargin_504d_base_v013_signal(ebitda, ebitdamargin):
    result = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda/revenue mean
def em_f053_ebitda_margin_per_revenue_63d_base_v014_signal(ebitda, revenue):
    result = _mean(_ebitda_margin_scaled(ebitda, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/revenue mean
def em_f053_ebitda_margin_per_revenue_252d_base_v015_signal(ebitda, revenue):
    result = _mean(_ebitda_margin_scaled(ebitda, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda/revenue mean
def em_f053_ebitda_margin_per_revenue_504d_base_v016_signal(ebitda, revenue):
    result = _mean(_ebitda_margin_scaled(ebitda, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda/assets mean
def em_f053_ebitda_margin_per_assets_63d_base_v017_signal(ebitda, assets):
    result = _mean(_ebitda_margin_scaled(ebitda, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/assets mean
def em_f053_ebitda_margin_per_assets_252d_base_v018_signal(ebitda, assets):
    result = _mean(_ebitda_margin_scaled(ebitda, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda/assets mean
def em_f053_ebitda_margin_per_assets_504d_base_v019_signal(ebitda, assets):
    result = _mean(_ebitda_margin_scaled(ebitda, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda/marketcap mean
def em_f053_ebitda_margin_per_marketcap_63d_base_v020_signal(ebitda, marketcap):
    result = _mean(_ebitda_margin_scaled(ebitda, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/marketcap mean
def em_f053_ebitda_margin_per_marketcap_252d_base_v021_signal(ebitda, marketcap):
    result = _mean(_ebitda_margin_scaled(ebitda, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda/marketcap mean
def em_f053_ebitda_margin_per_marketcap_504d_base_v022_signal(ebitda, marketcap):
    result = _mean(_ebitda_margin_scaled(ebitda, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda/equity mean
def em_f053_ebitda_margin_per_equity_63d_base_v023_signal(ebitda, equity):
    result = _mean(_ebitda_margin_scaled(ebitda, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/equity mean
def em_f053_ebitda_margin_per_equity_252d_base_v024_signal(ebitda, equity):
    result = _mean(_ebitda_margin_scaled(ebitda, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda/equity mean
def em_f053_ebitda_margin_per_equity_504d_base_v025_signal(ebitda, equity):
    result = _mean(_ebitda_margin_scaled(ebitda, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda per share times closeadj
def em_f053_ebitda_margin_pershare_21d_base_v026_signal(ebitda, sharesbas, closeadj):
    ps = _ebitda_margin_per_share(ebitda, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda per share times closeadj
def em_f053_ebitda_margin_pershare_63d_base_v027_signal(ebitda, sharesbas, closeadj):
    ps = _ebitda_margin_per_share(ebitda, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ebitda per share times closeadj
def em_f053_ebitda_margin_pershare_126d_base_v028_signal(ebitda, sharesbas, closeadj):
    ps = _ebitda_margin_per_share(ebitda, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda per share times closeadj
def em_f053_ebitda_margin_pershare_252d_base_v029_signal(ebitda, sharesbas, closeadj):
    ps = _ebitda_margin_per_share(ebitda, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda per share times closeadj
def em_f053_ebitda_margin_pershare_504d_base_v030_signal(ebitda, sharesbas, closeadj):
    ps = _ebitda_margin_per_share(ebitda, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of ebitda times closeadj
def em_f053_ebitda_margin_std_63d_base_v031_signal(ebitda, closeadj):
    result = _std(ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of ebitda times closeadj
def em_f053_ebitda_margin_std_252d_base_v032_signal(ebitda, closeadj):
    result = _std(ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of ebitda times closeadj
def em_f053_ebitda_margin_std_504d_base_v033_signal(ebitda, closeadj):
    result = _std(ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ebitda
def em_f053_ebitda_margin_z_252d_base_v034_signal(ebitda):
    result = _z(ebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ebitda
def em_f053_ebitda_margin_z_504d_base_v035_signal(ebitda):
    result = _z(ebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(ebitda)
def em_f053_ebitda_margin_logz_252d_base_v036_signal(ebitda):
    result = _z(_ebitda_margin_log(ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(ebitda)
def em_f053_ebitda_margin_logz_504d_base_v037_signal(ebitda):
    result = _z(_ebitda_margin_log(ebitda), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of ebitda^2 times closeadj
def em_f053_ebitda_margin_sq_63d_base_v038_signal(ebitda, closeadj):
    result = _mean(ebitda * ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of ebitda^2 times closeadj
def em_f053_ebitda_margin_sq_252d_base_v039_signal(ebitda, closeadj):
    result = _mean(ebitda * ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(ebitda) times closeadj
def em_f053_ebitda_margin_sign_21d_base_v040_signal(ebitda, closeadj):
    result = _mean(np.sign(ebitda), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(ebitda) times closeadj
def em_f053_ebitda_margin_sign_63d_base_v041_signal(ebitda, closeadj):
    result = _mean(np.sign(ebitda), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(ebitda) times closeadj
def em_f053_ebitda_margin_sign_252d_base_v042_signal(ebitda, closeadj):
    result = _mean(np.sign(ebitda), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda/opex mean
def em_f053_ebitda_margin_per_opex_63d_base_v043_signal(ebitda, opex):
    result = _mean(_ebitda_margin_scaled(ebitda, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/opex mean
def em_f053_ebitda_margin_per_opex_252d_base_v044_signal(ebitda, opex):
    result = _mean(_ebitda_margin_scaled(ebitda, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda/ebitda mean
def em_f053_ebitda_margin_per_ebitda_63d_base_v045_signal(ebitda):
    result = _mean(_ebitda_margin_scaled(ebitda, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/ebitda mean
def em_f053_ebitda_margin_per_ebitda_252d_base_v046_signal(ebitda):
    result = _mean(_ebitda_margin_scaled(ebitda, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda/capex mean
def em_f053_ebitda_margin_per_capex_63d_base_v047_signal(ebitda, capex):
    result = _mean(_ebitda_margin_scaled(ebitda, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/capex mean
def em_f053_ebitda_margin_per_capex_252d_base_v048_signal(ebitda, capex):
    result = _mean(_ebitda_margin_scaled(ebitda, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda/liabilities mean
def em_f053_ebitda_margin_per_liabilities_63d_base_v049_signal(ebitda, liabilities):
    result = _mean(_ebitda_margin_scaled(ebitda, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/liabilities mean
def em_f053_ebitda_margin_per_liabilities_252d_base_v050_signal(ebitda, liabilities):
    result = _mean(_ebitda_margin_scaled(ebitda, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda relative to 252d max times closeadj
def em_f053_ebitda_margin_relmax_252d_base_v051_signal(ebitda, closeadj):
    peak = ebitda.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (ebitda / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda relative to 504d max times closeadj
def em_f053_ebitda_margin_relmax_504d_base_v052_signal(ebitda, closeadj):
    peak = ebitda.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (ebitda / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda relative to 252d min times closeadj
def em_f053_ebitda_margin_relmin_252d_base_v053_signal(ebitda, closeadj):
    trough = ebitda.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (ebitda / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda relative to 504d min times closeadj
def em_f053_ebitda_margin_relmin_504d_base_v054_signal(ebitda, closeadj):
    trough = ebitda.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (ebitda / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of ebitda times closeadj
def em_f053_ebitda_margin_pct_21d_base_v055_signal(ebitda, closeadj):
    result = _pct_change(ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of ebitda times closeadj
def em_f053_ebitda_margin_pct_63d_base_v056_signal(ebitda, closeadj):
    result = _pct_change(ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of ebitda times closeadj
def em_f053_ebitda_margin_pct_252d_base_v057_signal(ebitda, closeadj):
    result = _pct_change(ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of ebitda times closeadj
def em_f053_ebitda_margin_sum_63d_base_v058_signal(ebitda, closeadj):
    result = ebitda.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of ebitda times closeadj
def em_f053_ebitda_margin_sum_252d_base_v059_signal(ebitda, closeadj):
    result = ebitda.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of ebitda times closeadj
def em_f053_ebitda_margin_sum_504d_base_v060_signal(ebitda, closeadj):
    result = ebitda.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ebitda(63d) / smoothed ebitdamargin(252d) x closeadj
def em_f053_ebitda_margin_rom_ebitdamargin_252_63d_base_v061_signal(ebitda, ebitdamargin, closeadj):
    n = _mean(ebitda, 63)
    d = _mean(ebitdamargin, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ebitda(126d) / smoothed ebitdamargin(504d) x closeadj
def em_f053_ebitda_margin_rom_ebitdamargin_504_126d_base_v062_signal(ebitda, ebitdamargin, closeadj):
    n = _mean(ebitda, 126)
    d = _mean(ebitdamargin, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ebitda(63d) / smoothed revenue(252d) x closeadj
def em_f053_ebitda_margin_rom_revenue_252_63d_base_v063_signal(ebitda, revenue, closeadj):
    n = _mean(ebitda, 63)
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ebitda(126d) / smoothed revenue(504d) x closeadj
def em_f053_ebitda_margin_rom_revenue_504_126d_base_v064_signal(ebitda, revenue, closeadj):
    n = _mean(ebitda, 126)
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ebitda(63d) / smoothed assets(252d) x closeadj
def em_f053_ebitda_margin_rom_assets_252_63d_base_v065_signal(ebitda, assets, closeadj):
    n = _mean(ebitda, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ebitda(126d) / smoothed assets(504d) x closeadj
def em_f053_ebitda_margin_rom_assets_504_126d_base_v066_signal(ebitda, assets, closeadj):
    n = _mean(ebitda, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ebitda) / std(ebitdamargin)
def em_f053_ebitda_margin_volratio_ebitdamargin_252d_base_v067_signal(ebitda, ebitdamargin):
    n = _std(ebitda, 252)
    d = _std(ebitdamargin, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ebitda) / std(ebitdamargin)
def em_f053_ebitda_margin_volratio_ebitdamargin_504d_base_v068_signal(ebitda, ebitdamargin):
    n = _std(ebitda, 504)
    d = _std(ebitdamargin, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ebitda) / std(revenue)
def em_f053_ebitda_margin_volratio_revenue_252d_base_v069_signal(ebitda, revenue):
    n = _std(ebitda, 252)
    d = _std(revenue, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ebitda) / std(revenue)
def em_f053_ebitda_margin_volratio_revenue_504d_base_v070_signal(ebitda, revenue):
    n = _std(ebitda, 504)
    d = _std(revenue, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed ebitda times closeadj
def em_f053_ebitda_margin_raw_5d_base_v071_signal(ebitda, closeadj):
    result = _mean(ebitda, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed ebitda times closeadj
def em_f053_ebitda_margin_raw_1008d_base_v072_signal(ebitda, closeadj):
    result = _mean(ebitda, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ebitda/ebitdamargin
def em_f053_ebitda_margin_log_per_ebitdamargin_252d_base_v073_signal(ebitda, ebitdamargin):
    s = _ebitda_margin_scaled(ebitda, ebitdamargin)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ebitda/ebitdamargin
def em_f053_ebitda_margin_log_per_ebitdamargin_504d_base_v074_signal(ebitda, ebitdamargin):
    s = _ebitda_margin_scaled(ebitda, ebitdamargin)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ebitda/revenue
def em_f053_ebitda_margin_log_per_revenue_252d_base_v075_signal(ebitda, revenue):
    s = _ebitda_margin_scaled(ebitda, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
