"""Family f53 - Margin improvement rate  (H_Margins) | base 001-075"""
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


# 21d smoothed grossmargin times closeadj
def mi_f53_margin_improvement_raw_21d_base_v001_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed grossmargin times closeadj
def mi_f53_margin_improvement_raw_63d_base_v002_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed grossmargin times closeadj
def mi_f53_margin_improvement_raw_126d_base_v003_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed grossmargin times closeadj
def mi_f53_margin_improvement_raw_252d_base_v004_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed grossmargin times closeadj
def mi_f53_margin_improvement_raw_504d_base_v005_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(grossmargin) times closeadj
def mi_f53_margin_improvement_log_21d_base_v006_signal(grossmargin, closeadj):
    result = _mean(_margin_improvement_log(grossmargin), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(grossmargin) times closeadj
def mi_f53_margin_improvement_log_63d_base_v007_signal(grossmargin, closeadj):
    result = _mean(_margin_improvement_log(grossmargin), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(grossmargin) times closeadj
def mi_f53_margin_improvement_log_126d_base_v008_signal(grossmargin, closeadj):
    result = _mean(_margin_improvement_log(grossmargin), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(grossmargin) times closeadj
def mi_f53_margin_improvement_log_252d_base_v009_signal(grossmargin, closeadj):
    result = _mean(_margin_improvement_log(grossmargin), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(grossmargin) times closeadj
def mi_f53_margin_improvement_log_504d_base_v010_signal(grossmargin, closeadj):
    result = _mean(_margin_improvement_log(grossmargin), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin/assets mean
def mi_f53_margin_improvement_per_assets_63d_base_v011_signal(grossmargin, assets):
    result = _mean(_margin_improvement_scaled(grossmargin, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin/assets mean
def mi_f53_margin_improvement_per_assets_252d_base_v012_signal(grossmargin, assets):
    result = _mean(_margin_improvement_scaled(grossmargin, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d grossmargin/assets mean
def mi_f53_margin_improvement_per_assets_504d_base_v013_signal(grossmargin, assets):
    result = _mean(_margin_improvement_scaled(grossmargin, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin/marketcap mean
def mi_f53_margin_improvement_per_marketcap_63d_base_v014_signal(grossmargin, marketcap):
    result = _mean(_margin_improvement_scaled(grossmargin, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin/marketcap mean
def mi_f53_margin_improvement_per_marketcap_252d_base_v015_signal(grossmargin, marketcap):
    result = _mean(_margin_improvement_scaled(grossmargin, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d grossmargin/marketcap mean
def mi_f53_margin_improvement_per_marketcap_504d_base_v016_signal(grossmargin, marketcap):
    result = _mean(_margin_improvement_scaled(grossmargin, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin/equity mean
def mi_f53_margin_improvement_per_equity_63d_base_v017_signal(grossmargin, equity):
    result = _mean(_margin_improvement_scaled(grossmargin, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin/equity mean
def mi_f53_margin_improvement_per_equity_252d_base_v018_signal(grossmargin, equity):
    result = _mean(_margin_improvement_scaled(grossmargin, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d grossmargin/equity mean
def mi_f53_margin_improvement_per_equity_504d_base_v019_signal(grossmargin, equity):
    result = _mean(_margin_improvement_scaled(grossmargin, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin/debt mean
def mi_f53_margin_improvement_per_debt_63d_base_v020_signal(grossmargin, debt):
    result = _mean(_margin_improvement_scaled(grossmargin, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin/debt mean
def mi_f53_margin_improvement_per_debt_252d_base_v021_signal(grossmargin, debt):
    result = _mean(_margin_improvement_scaled(grossmargin, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d grossmargin/debt mean
def mi_f53_margin_improvement_per_debt_504d_base_v022_signal(grossmargin, debt):
    result = _mean(_margin_improvement_scaled(grossmargin, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin/revenue mean
def mi_f53_margin_improvement_per_revenue_63d_base_v023_signal(grossmargin, revenue):
    result = _mean(_margin_improvement_scaled(grossmargin, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin/revenue mean
def mi_f53_margin_improvement_per_revenue_252d_base_v024_signal(grossmargin, revenue):
    result = _mean(_margin_improvement_scaled(grossmargin, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d grossmargin/revenue mean
def mi_f53_margin_improvement_per_revenue_504d_base_v025_signal(grossmargin, revenue):
    result = _mean(_margin_improvement_scaled(grossmargin, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d grossmargin per share times closeadj
def mi_f53_margin_improvement_pershare_21d_base_v026_signal(grossmargin, sharesbas, closeadj):
    ps = _margin_improvement_per_share(grossmargin, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin per share times closeadj
def mi_f53_margin_improvement_pershare_63d_base_v027_signal(grossmargin, sharesbas, closeadj):
    ps = _margin_improvement_per_share(grossmargin, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d grossmargin per share times closeadj
def mi_f53_margin_improvement_pershare_126d_base_v028_signal(grossmargin, sharesbas, closeadj):
    ps = _margin_improvement_per_share(grossmargin, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin per share times closeadj
def mi_f53_margin_improvement_pershare_252d_base_v029_signal(grossmargin, sharesbas, closeadj):
    ps = _margin_improvement_per_share(grossmargin, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d grossmargin per share times closeadj
def mi_f53_margin_improvement_pershare_504d_base_v030_signal(grossmargin, sharesbas, closeadj):
    ps = _margin_improvement_per_share(grossmargin, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of grossmargin times closeadj
def mi_f53_margin_improvement_std_63d_base_v031_signal(grossmargin, closeadj):
    result = _std(grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of grossmargin times closeadj
def mi_f53_margin_improvement_std_252d_base_v032_signal(grossmargin, closeadj):
    result = _std(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of grossmargin times closeadj
def mi_f53_margin_improvement_std_504d_base_v033_signal(grossmargin, closeadj):
    result = _std(grossmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of grossmargin
def mi_f53_margin_improvement_z_252d_base_v034_signal(grossmargin):
    result = _z(grossmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of grossmargin
def mi_f53_margin_improvement_z_504d_base_v035_signal(grossmargin):
    result = _z(grossmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(grossmargin)
def mi_f53_margin_improvement_logz_252d_base_v036_signal(grossmargin):
    result = _z(_margin_improvement_log(grossmargin), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(grossmargin)
def mi_f53_margin_improvement_logz_504d_base_v037_signal(grossmargin):
    result = _z(_margin_improvement_log(grossmargin), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of grossmargin^2 times closeadj
def mi_f53_margin_improvement_sq_63d_base_v038_signal(grossmargin, closeadj):
    result = _mean(grossmargin * grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of grossmargin^2 times closeadj
def mi_f53_margin_improvement_sq_252d_base_v039_signal(grossmargin, closeadj):
    result = _mean(grossmargin * grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(grossmargin) times closeadj
def mi_f53_margin_improvement_sign_21d_base_v040_signal(grossmargin, closeadj):
    result = _mean(np.sign(grossmargin), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(grossmargin) times closeadj
def mi_f53_margin_improvement_sign_63d_base_v041_signal(grossmargin, closeadj):
    result = _mean(np.sign(grossmargin), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(grossmargin) times closeadj
def mi_f53_margin_improvement_sign_252d_base_v042_signal(grossmargin, closeadj):
    result = _mean(np.sign(grossmargin), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin/opex mean
def mi_f53_margin_improvement_per_opex_63d_base_v043_signal(grossmargin, opex):
    result = _mean(_margin_improvement_scaled(grossmargin, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin/opex mean
def mi_f53_margin_improvement_per_opex_252d_base_v044_signal(grossmargin, opex):
    result = _mean(_margin_improvement_scaled(grossmargin, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin/ebitda mean
def mi_f53_margin_improvement_per_ebitda_63d_base_v045_signal(grossmargin, ebitda):
    result = _mean(_margin_improvement_scaled(grossmargin, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin/ebitda mean
def mi_f53_margin_improvement_per_ebitda_252d_base_v046_signal(grossmargin, ebitda):
    result = _mean(_margin_improvement_scaled(grossmargin, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin/capex mean
def mi_f53_margin_improvement_per_capex_63d_base_v047_signal(grossmargin, capex):
    result = _mean(_margin_improvement_scaled(grossmargin, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin/capex mean
def mi_f53_margin_improvement_per_capex_252d_base_v048_signal(grossmargin, capex):
    result = _mean(_margin_improvement_scaled(grossmargin, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d grossmargin/liabilities mean
def mi_f53_margin_improvement_per_liabilities_63d_base_v049_signal(grossmargin, liabilities):
    result = _mean(_margin_improvement_scaled(grossmargin, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d grossmargin/liabilities mean
def mi_f53_margin_improvement_per_liabilities_252d_base_v050_signal(grossmargin, liabilities):
    result = _mean(_margin_improvement_scaled(grossmargin, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# grossmargin relative to 252d max times closeadj
def mi_f53_margin_improvement_relmax_252d_base_v051_signal(grossmargin, closeadj):
    peak = grossmargin.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (grossmargin / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# grossmargin relative to 504d max times closeadj
def mi_f53_margin_improvement_relmax_504d_base_v052_signal(grossmargin, closeadj):
    peak = grossmargin.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (grossmargin / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# grossmargin relative to 252d min times closeadj
def mi_f53_margin_improvement_relmin_252d_base_v053_signal(grossmargin, closeadj):
    trough = grossmargin.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (grossmargin / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# grossmargin relative to 504d min times closeadj
def mi_f53_margin_improvement_relmin_504d_base_v054_signal(grossmargin, closeadj):
    trough = grossmargin.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (grossmargin / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of grossmargin times closeadj
def mi_f53_margin_improvement_pct_21d_base_v055_signal(grossmargin, closeadj):
    result = _pct_change(grossmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of grossmargin times closeadj
def mi_f53_margin_improvement_pct_63d_base_v056_signal(grossmargin, closeadj):
    result = _pct_change(grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of grossmargin times closeadj
def mi_f53_margin_improvement_pct_252d_base_v057_signal(grossmargin, closeadj):
    result = _pct_change(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of grossmargin times closeadj
def mi_f53_margin_improvement_sum_63d_base_v058_signal(grossmargin, closeadj):
    result = grossmargin.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of grossmargin times closeadj
def mi_f53_margin_improvement_sum_252d_base_v059_signal(grossmargin, closeadj):
    result = grossmargin.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of grossmargin times closeadj
def mi_f53_margin_improvement_sum_504d_base_v060_signal(grossmargin, closeadj):
    result = grossmargin.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed grossmargin(63d) / smoothed assets(252d) x closeadj
def mi_f53_margin_improvement_rom_assets_252_63d_base_v061_signal(grossmargin, assets, closeadj):
    n = _mean(grossmargin, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed grossmargin(126d) / smoothed assets(504d) x closeadj
def mi_f53_margin_improvement_rom_assets_504_126d_base_v062_signal(grossmargin, assets, closeadj):
    n = _mean(grossmargin, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed grossmargin(63d) / smoothed marketcap(252d) x closeadj
def mi_f53_margin_improvement_rom_marketcap_252_63d_base_v063_signal(grossmargin, marketcap, closeadj):
    n = _mean(grossmargin, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed grossmargin(126d) / smoothed marketcap(504d) x closeadj
def mi_f53_margin_improvement_rom_marketcap_504_126d_base_v064_signal(grossmargin, marketcap, closeadj):
    n = _mean(grossmargin, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed grossmargin(63d) / smoothed equity(252d) x closeadj
def mi_f53_margin_improvement_rom_equity_252_63d_base_v065_signal(grossmargin, equity, closeadj):
    n = _mean(grossmargin, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed grossmargin(126d) / smoothed equity(504d) x closeadj
def mi_f53_margin_improvement_rom_equity_504_126d_base_v066_signal(grossmargin, equity, closeadj):
    n = _mean(grossmargin, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(grossmargin) / std(assets)
def mi_f53_margin_improvement_volratio_assets_252d_base_v067_signal(grossmargin, assets):
    n = _std(grossmargin, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(grossmargin) / std(assets)
def mi_f53_margin_improvement_volratio_assets_504d_base_v068_signal(grossmargin, assets):
    n = _std(grossmargin, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(grossmargin) / std(marketcap)
def mi_f53_margin_improvement_volratio_marketcap_252d_base_v069_signal(grossmargin, marketcap):
    n = _std(grossmargin, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(grossmargin) / std(marketcap)
def mi_f53_margin_improvement_volratio_marketcap_504d_base_v070_signal(grossmargin, marketcap):
    n = _std(grossmargin, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed grossmargin times closeadj
def mi_f53_margin_improvement_raw_5d_base_v071_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed grossmargin times closeadj
def mi_f53_margin_improvement_raw_1008d_base_v072_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of grossmargin/assets
def mi_f53_margin_improvement_log_per_assets_252d_base_v073_signal(grossmargin, assets):
    s = _margin_improvement_scaled(grossmargin, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of grossmargin/assets
def mi_f53_margin_improvement_log_per_assets_504d_base_v074_signal(grossmargin, assets):
    s = _margin_improvement_scaled(grossmargin, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of grossmargin/marketcap
def mi_f53_margin_improvement_log_per_marketcap_252d_base_v075_signal(grossmargin, marketcap):
    s = _margin_improvement_scaled(grossmargin, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
