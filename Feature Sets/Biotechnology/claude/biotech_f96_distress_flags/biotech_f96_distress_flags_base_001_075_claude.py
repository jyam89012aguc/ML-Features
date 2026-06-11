"""Family f96 - Distress & structural flags  (Q_Actions_Events) | base 001-075"""
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
def _distress_flags_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _distress_flags_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _distress_flags_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed distressflag times closeadj
def df_f96_distress_flags_raw_21d_base_v001_signal(distressflag, closeadj):
    result = _mean(distressflag, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed distressflag times closeadj
def df_f96_distress_flags_raw_63d_base_v002_signal(distressflag, closeadj):
    result = _mean(distressflag, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed distressflag times closeadj
def df_f96_distress_flags_raw_126d_base_v003_signal(distressflag, closeadj):
    result = _mean(distressflag, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed distressflag times closeadj
def df_f96_distress_flags_raw_252d_base_v004_signal(distressflag, closeadj):
    result = _mean(distressflag, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed distressflag times closeadj
def df_f96_distress_flags_raw_504d_base_v005_signal(distressflag, closeadj):
    result = _mean(distressflag, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(distressflag) times closeadj
def df_f96_distress_flags_log_21d_base_v006_signal(distressflag, closeadj):
    result = _mean(_distress_flags_log(distressflag), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(distressflag) times closeadj
def df_f96_distress_flags_log_63d_base_v007_signal(distressflag, closeadj):
    result = _mean(_distress_flags_log(distressflag), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(distressflag) times closeadj
def df_f96_distress_flags_log_126d_base_v008_signal(distressflag, closeadj):
    result = _mean(_distress_flags_log(distressflag), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(distressflag) times closeadj
def df_f96_distress_flags_log_252d_base_v009_signal(distressflag, closeadj):
    result = _mean(_distress_flags_log(distressflag), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(distressflag) times closeadj
def df_f96_distress_flags_log_504d_base_v010_signal(distressflag, closeadj):
    result = _mean(_distress_flags_log(distressflag), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag/assets mean
def df_f96_distress_flags_per_assets_63d_base_v011_signal(distressflag, assets):
    result = _mean(_distress_flags_scaled(distressflag, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag/assets mean
def df_f96_distress_flags_per_assets_252d_base_v012_signal(distressflag, assets):
    result = _mean(_distress_flags_scaled(distressflag, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distressflag/assets mean
def df_f96_distress_flags_per_assets_504d_base_v013_signal(distressflag, assets):
    result = _mean(_distress_flags_scaled(distressflag, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag/marketcap mean
def df_f96_distress_flags_per_marketcap_63d_base_v014_signal(distressflag, marketcap):
    result = _mean(_distress_flags_scaled(distressflag, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag/marketcap mean
def df_f96_distress_flags_per_marketcap_252d_base_v015_signal(distressflag, marketcap):
    result = _mean(_distress_flags_scaled(distressflag, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distressflag/marketcap mean
def df_f96_distress_flags_per_marketcap_504d_base_v016_signal(distressflag, marketcap):
    result = _mean(_distress_flags_scaled(distressflag, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag/equity mean
def df_f96_distress_flags_per_equity_63d_base_v017_signal(distressflag, equity):
    result = _mean(_distress_flags_scaled(distressflag, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag/equity mean
def df_f96_distress_flags_per_equity_252d_base_v018_signal(distressflag, equity):
    result = _mean(_distress_flags_scaled(distressflag, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distressflag/equity mean
def df_f96_distress_flags_per_equity_504d_base_v019_signal(distressflag, equity):
    result = _mean(_distress_flags_scaled(distressflag, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag/debt mean
def df_f96_distress_flags_per_debt_63d_base_v020_signal(distressflag, debt):
    result = _mean(_distress_flags_scaled(distressflag, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag/debt mean
def df_f96_distress_flags_per_debt_252d_base_v021_signal(distressflag, debt):
    result = _mean(_distress_flags_scaled(distressflag, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distressflag/debt mean
def df_f96_distress_flags_per_debt_504d_base_v022_signal(distressflag, debt):
    result = _mean(_distress_flags_scaled(distressflag, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag/revenue mean
def df_f96_distress_flags_per_revenue_63d_base_v023_signal(distressflag, revenue):
    result = _mean(_distress_flags_scaled(distressflag, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag/revenue mean
def df_f96_distress_flags_per_revenue_252d_base_v024_signal(distressflag, revenue):
    result = _mean(_distress_flags_scaled(distressflag, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distressflag/revenue mean
def df_f96_distress_flags_per_revenue_504d_base_v025_signal(distressflag, revenue):
    result = _mean(_distress_flags_scaled(distressflag, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d distressflag per share times closeadj
def df_f96_distress_flags_pershare_21d_base_v026_signal(distressflag, sharesbas, closeadj):
    ps = _distress_flags_per_share(distressflag, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag per share times closeadj
def df_f96_distress_flags_pershare_63d_base_v027_signal(distressflag, sharesbas, closeadj):
    ps = _distress_flags_per_share(distressflag, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d distressflag per share times closeadj
def df_f96_distress_flags_pershare_126d_base_v028_signal(distressflag, sharesbas, closeadj):
    ps = _distress_flags_per_share(distressflag, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag per share times closeadj
def df_f96_distress_flags_pershare_252d_base_v029_signal(distressflag, sharesbas, closeadj):
    ps = _distress_flags_per_share(distressflag, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distressflag per share times closeadj
def df_f96_distress_flags_pershare_504d_base_v030_signal(distressflag, sharesbas, closeadj):
    ps = _distress_flags_per_share(distressflag, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of distressflag times closeadj
def df_f96_distress_flags_std_63d_base_v031_signal(distressflag, closeadj):
    result = _std(distressflag, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of distressflag times closeadj
def df_f96_distress_flags_std_252d_base_v032_signal(distressflag, closeadj):
    result = _std(distressflag, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of distressflag times closeadj
def df_f96_distress_flags_std_504d_base_v033_signal(distressflag, closeadj):
    result = _std(distressflag, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of distressflag
def df_f96_distress_flags_z_252d_base_v034_signal(distressflag):
    result = _z(distressflag, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of distressflag
def df_f96_distress_flags_z_504d_base_v035_signal(distressflag):
    result = _z(distressflag, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(distressflag)
def df_f96_distress_flags_logz_252d_base_v036_signal(distressflag):
    result = _z(_distress_flags_log(distressflag), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(distressflag)
def df_f96_distress_flags_logz_504d_base_v037_signal(distressflag):
    result = _z(_distress_flags_log(distressflag), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of distressflag^2 times closeadj
def df_f96_distress_flags_sq_63d_base_v038_signal(distressflag, closeadj):
    result = _mean(distressflag * distressflag, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of distressflag^2 times closeadj
def df_f96_distress_flags_sq_252d_base_v039_signal(distressflag, closeadj):
    result = _mean(distressflag * distressflag, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(distressflag) times closeadj
def df_f96_distress_flags_sign_21d_base_v040_signal(distressflag, closeadj):
    result = _mean(np.sign(distressflag), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(distressflag) times closeadj
def df_f96_distress_flags_sign_63d_base_v041_signal(distressflag, closeadj):
    result = _mean(np.sign(distressflag), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(distressflag) times closeadj
def df_f96_distress_flags_sign_252d_base_v042_signal(distressflag, closeadj):
    result = _mean(np.sign(distressflag), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag/opex mean
def df_f96_distress_flags_per_opex_63d_base_v043_signal(distressflag, opex):
    result = _mean(_distress_flags_scaled(distressflag, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag/opex mean
def df_f96_distress_flags_per_opex_252d_base_v044_signal(distressflag, opex):
    result = _mean(_distress_flags_scaled(distressflag, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag/ebitda mean
def df_f96_distress_flags_per_ebitda_63d_base_v045_signal(distressflag, ebitda):
    result = _mean(_distress_flags_scaled(distressflag, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag/ebitda mean
def df_f96_distress_flags_per_ebitda_252d_base_v046_signal(distressflag, ebitda):
    result = _mean(_distress_flags_scaled(distressflag, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag/capex mean
def df_f96_distress_flags_per_capex_63d_base_v047_signal(distressflag, capex):
    result = _mean(_distress_flags_scaled(distressflag, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag/capex mean
def df_f96_distress_flags_per_capex_252d_base_v048_signal(distressflag, capex):
    result = _mean(_distress_flags_scaled(distressflag, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distressflag/liabilities mean
def df_f96_distress_flags_per_liabilities_63d_base_v049_signal(distressflag, liabilities):
    result = _mean(_distress_flags_scaled(distressflag, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distressflag/liabilities mean
def df_f96_distress_flags_per_liabilities_252d_base_v050_signal(distressflag, liabilities):
    result = _mean(_distress_flags_scaled(distressflag, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# distressflag relative to 252d max times closeadj
def df_f96_distress_flags_relmax_252d_base_v051_signal(distressflag, closeadj):
    peak = distressflag.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (distressflag / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distressflag relative to 504d max times closeadj
def df_f96_distress_flags_relmax_504d_base_v052_signal(distressflag, closeadj):
    peak = distressflag.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (distressflag / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distressflag relative to 252d min times closeadj
def df_f96_distress_flags_relmin_252d_base_v053_signal(distressflag, closeadj):
    trough = distressflag.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (distressflag / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distressflag relative to 504d min times closeadj
def df_f96_distress_flags_relmin_504d_base_v054_signal(distressflag, closeadj):
    trough = distressflag.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (distressflag / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of distressflag times closeadj
def df_f96_distress_flags_pct_21d_base_v055_signal(distressflag, closeadj):
    result = _pct_change(distressflag, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of distressflag times closeadj
def df_f96_distress_flags_pct_63d_base_v056_signal(distressflag, closeadj):
    result = _pct_change(distressflag, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of distressflag times closeadj
def df_f96_distress_flags_pct_252d_base_v057_signal(distressflag, closeadj):
    result = _pct_change(distressflag, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of distressflag times closeadj
def df_f96_distress_flags_sum_63d_base_v058_signal(distressflag, closeadj):
    result = distressflag.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of distressflag times closeadj
def df_f96_distress_flags_sum_252d_base_v059_signal(distressflag, closeadj):
    result = distressflag.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of distressflag times closeadj
def df_f96_distress_flags_sum_504d_base_v060_signal(distressflag, closeadj):
    result = distressflag.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed distressflag(63d) / smoothed assets(252d) x closeadj
def df_f96_distress_flags_rom_assets_252_63d_base_v061_signal(distressflag, assets, closeadj):
    n = _mean(distressflag, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed distressflag(126d) / smoothed assets(504d) x closeadj
def df_f96_distress_flags_rom_assets_504_126d_base_v062_signal(distressflag, assets, closeadj):
    n = _mean(distressflag, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed distressflag(63d) / smoothed marketcap(252d) x closeadj
def df_f96_distress_flags_rom_marketcap_252_63d_base_v063_signal(distressflag, marketcap, closeadj):
    n = _mean(distressflag, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed distressflag(126d) / smoothed marketcap(504d) x closeadj
def df_f96_distress_flags_rom_marketcap_504_126d_base_v064_signal(distressflag, marketcap, closeadj):
    n = _mean(distressflag, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed distressflag(63d) / smoothed equity(252d) x closeadj
def df_f96_distress_flags_rom_equity_252_63d_base_v065_signal(distressflag, equity, closeadj):
    n = _mean(distressflag, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed distressflag(126d) / smoothed equity(504d) x closeadj
def df_f96_distress_flags_rom_equity_504_126d_base_v066_signal(distressflag, equity, closeadj):
    n = _mean(distressflag, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(distressflag) / std(assets)
def df_f96_distress_flags_volratio_assets_252d_base_v067_signal(distressflag, assets):
    n = _std(distressflag, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(distressflag) / std(assets)
def df_f96_distress_flags_volratio_assets_504d_base_v068_signal(distressflag, assets):
    n = _std(distressflag, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(distressflag) / std(marketcap)
def df_f96_distress_flags_volratio_marketcap_252d_base_v069_signal(distressflag, marketcap):
    n = _std(distressflag, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(distressflag) / std(marketcap)
def df_f96_distress_flags_volratio_marketcap_504d_base_v070_signal(distressflag, marketcap):
    n = _std(distressflag, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed distressflag times closeadj
def df_f96_distress_flags_raw_5d_base_v071_signal(distressflag, closeadj):
    result = _mean(distressflag, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed distressflag times closeadj
def df_f96_distress_flags_raw_1008d_base_v072_signal(distressflag, closeadj):
    result = _mean(distressflag, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of distressflag/assets
def df_f96_distress_flags_log_per_assets_252d_base_v073_signal(distressflag, assets):
    s = _distress_flags_scaled(distressflag, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of distressflag/assets
def df_f96_distress_flags_log_per_assets_504d_base_v074_signal(distressflag, assets):
    s = _distress_flags_scaled(distressflag, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of distressflag/marketcap
def df_f96_distress_flags_log_per_marketcap_252d_base_v075_signal(distressflag, marketcap):
    s = _distress_flags_scaled(distressflag, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
