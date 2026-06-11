"""Family f38 - Tangible book value  (F_BalanceSheet) | base 001-075"""
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
def _tangible_book_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _tangible_book_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _tangible_book_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed tangibles times closeadj
def tb_f38_tangible_book_raw_21d_base_v001_signal(tangibles, closeadj):
    result = _mean(tangibles, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed tangibles times closeadj
def tb_f38_tangible_book_raw_63d_base_v002_signal(tangibles, closeadj):
    result = _mean(tangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed tangibles times closeadj
def tb_f38_tangible_book_raw_126d_base_v003_signal(tangibles, closeadj):
    result = _mean(tangibles, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed tangibles times closeadj
def tb_f38_tangible_book_raw_252d_base_v004_signal(tangibles, closeadj):
    result = _mean(tangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed tangibles times closeadj
def tb_f38_tangible_book_raw_504d_base_v005_signal(tangibles, closeadj):
    result = _mean(tangibles, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(tangibles) times closeadj
def tb_f38_tangible_book_log_21d_base_v006_signal(tangibles, closeadj):
    result = _mean(_tangible_book_log(tangibles), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(tangibles) times closeadj
def tb_f38_tangible_book_log_63d_base_v007_signal(tangibles, closeadj):
    result = _mean(_tangible_book_log(tangibles), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(tangibles) times closeadj
def tb_f38_tangible_book_log_126d_base_v008_signal(tangibles, closeadj):
    result = _mean(_tangible_book_log(tangibles), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(tangibles) times closeadj
def tb_f38_tangible_book_log_252d_base_v009_signal(tangibles, closeadj):
    result = _mean(_tangible_book_log(tangibles), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(tangibles) times closeadj
def tb_f38_tangible_book_log_504d_base_v010_signal(tangibles, closeadj):
    result = _mean(_tangible_book_log(tangibles), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles/assets mean
def tb_f38_tangible_book_per_assets_63d_base_v011_signal(tangibles, assets):
    result = _mean(_tangible_book_scaled(tangibles, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles/assets mean
def tb_f38_tangible_book_per_assets_252d_base_v012_signal(tangibles, assets):
    result = _mean(_tangible_book_scaled(tangibles, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tangibles/assets mean
def tb_f38_tangible_book_per_assets_504d_base_v013_signal(tangibles, assets):
    result = _mean(_tangible_book_scaled(tangibles, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles/marketcap mean
def tb_f38_tangible_book_per_marketcap_63d_base_v014_signal(tangibles, marketcap):
    result = _mean(_tangible_book_scaled(tangibles, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles/marketcap mean
def tb_f38_tangible_book_per_marketcap_252d_base_v015_signal(tangibles, marketcap):
    result = _mean(_tangible_book_scaled(tangibles, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tangibles/marketcap mean
def tb_f38_tangible_book_per_marketcap_504d_base_v016_signal(tangibles, marketcap):
    result = _mean(_tangible_book_scaled(tangibles, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles/equity mean
def tb_f38_tangible_book_per_equity_63d_base_v017_signal(tangibles, equity):
    result = _mean(_tangible_book_scaled(tangibles, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles/equity mean
def tb_f38_tangible_book_per_equity_252d_base_v018_signal(tangibles, equity):
    result = _mean(_tangible_book_scaled(tangibles, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tangibles/equity mean
def tb_f38_tangible_book_per_equity_504d_base_v019_signal(tangibles, equity):
    result = _mean(_tangible_book_scaled(tangibles, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles/debt mean
def tb_f38_tangible_book_per_debt_63d_base_v020_signal(tangibles, debt):
    result = _mean(_tangible_book_scaled(tangibles, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles/debt mean
def tb_f38_tangible_book_per_debt_252d_base_v021_signal(tangibles, debt):
    result = _mean(_tangible_book_scaled(tangibles, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tangibles/debt mean
def tb_f38_tangible_book_per_debt_504d_base_v022_signal(tangibles, debt):
    result = _mean(_tangible_book_scaled(tangibles, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles/revenue mean
def tb_f38_tangible_book_per_revenue_63d_base_v023_signal(tangibles, revenue):
    result = _mean(_tangible_book_scaled(tangibles, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles/revenue mean
def tb_f38_tangible_book_per_revenue_252d_base_v024_signal(tangibles, revenue):
    result = _mean(_tangible_book_scaled(tangibles, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tangibles/revenue mean
def tb_f38_tangible_book_per_revenue_504d_base_v025_signal(tangibles, revenue):
    result = _mean(_tangible_book_scaled(tangibles, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d tangibles per share times closeadj
def tb_f38_tangible_book_pershare_21d_base_v026_signal(tangibles, sharesbas, closeadj):
    ps = _tangible_book_per_share(tangibles, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles per share times closeadj
def tb_f38_tangible_book_pershare_63d_base_v027_signal(tangibles, sharesbas, closeadj):
    ps = _tangible_book_per_share(tangibles, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d tangibles per share times closeadj
def tb_f38_tangible_book_pershare_126d_base_v028_signal(tangibles, sharesbas, closeadj):
    ps = _tangible_book_per_share(tangibles, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles per share times closeadj
def tb_f38_tangible_book_pershare_252d_base_v029_signal(tangibles, sharesbas, closeadj):
    ps = _tangible_book_per_share(tangibles, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tangibles per share times closeadj
def tb_f38_tangible_book_pershare_504d_base_v030_signal(tangibles, sharesbas, closeadj):
    ps = _tangible_book_per_share(tangibles, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of tangibles times closeadj
def tb_f38_tangible_book_std_63d_base_v031_signal(tangibles, closeadj):
    result = _std(tangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of tangibles times closeadj
def tb_f38_tangible_book_std_252d_base_v032_signal(tangibles, closeadj):
    result = _std(tangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of tangibles times closeadj
def tb_f38_tangible_book_std_504d_base_v033_signal(tangibles, closeadj):
    result = _std(tangibles, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of tangibles
def tb_f38_tangible_book_z_252d_base_v034_signal(tangibles):
    result = _z(tangibles, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of tangibles
def tb_f38_tangible_book_z_504d_base_v035_signal(tangibles):
    result = _z(tangibles, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(tangibles)
def tb_f38_tangible_book_logz_252d_base_v036_signal(tangibles):
    result = _z(_tangible_book_log(tangibles), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(tangibles)
def tb_f38_tangible_book_logz_504d_base_v037_signal(tangibles):
    result = _z(_tangible_book_log(tangibles), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of tangibles^2 times closeadj
def tb_f38_tangible_book_sq_63d_base_v038_signal(tangibles, closeadj):
    result = _mean(tangibles * tangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of tangibles^2 times closeadj
def tb_f38_tangible_book_sq_252d_base_v039_signal(tangibles, closeadj):
    result = _mean(tangibles * tangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(tangibles) times closeadj
def tb_f38_tangible_book_sign_21d_base_v040_signal(tangibles, closeadj):
    result = _mean(np.sign(tangibles), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(tangibles) times closeadj
def tb_f38_tangible_book_sign_63d_base_v041_signal(tangibles, closeadj):
    result = _mean(np.sign(tangibles), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(tangibles) times closeadj
def tb_f38_tangible_book_sign_252d_base_v042_signal(tangibles, closeadj):
    result = _mean(np.sign(tangibles), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles/opex mean
def tb_f38_tangible_book_per_opex_63d_base_v043_signal(tangibles, opex):
    result = _mean(_tangible_book_scaled(tangibles, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles/opex mean
def tb_f38_tangible_book_per_opex_252d_base_v044_signal(tangibles, opex):
    result = _mean(_tangible_book_scaled(tangibles, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles/ebitda mean
def tb_f38_tangible_book_per_ebitda_63d_base_v045_signal(tangibles, ebitda):
    result = _mean(_tangible_book_scaled(tangibles, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles/ebitda mean
def tb_f38_tangible_book_per_ebitda_252d_base_v046_signal(tangibles, ebitda):
    result = _mean(_tangible_book_scaled(tangibles, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles/capex mean
def tb_f38_tangible_book_per_capex_63d_base_v047_signal(tangibles, capex):
    result = _mean(_tangible_book_scaled(tangibles, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles/capex mean
def tb_f38_tangible_book_per_capex_252d_base_v048_signal(tangibles, capex):
    result = _mean(_tangible_book_scaled(tangibles, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tangibles/liabilities mean
def tb_f38_tangible_book_per_liabilities_63d_base_v049_signal(tangibles, liabilities):
    result = _mean(_tangible_book_scaled(tangibles, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangibles/liabilities mean
def tb_f38_tangible_book_per_liabilities_252d_base_v050_signal(tangibles, liabilities):
    result = _mean(_tangible_book_scaled(tangibles, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles relative to 252d max times closeadj
def tb_f38_tangible_book_relmax_252d_base_v051_signal(tangibles, closeadj):
    peak = tangibles.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (tangibles / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles relative to 504d max times closeadj
def tb_f38_tangible_book_relmax_504d_base_v052_signal(tangibles, closeadj):
    peak = tangibles.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (tangibles / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles relative to 252d min times closeadj
def tb_f38_tangible_book_relmin_252d_base_v053_signal(tangibles, closeadj):
    trough = tangibles.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (tangibles / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles relative to 504d min times closeadj
def tb_f38_tangible_book_relmin_504d_base_v054_signal(tangibles, closeadj):
    trough = tangibles.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (tangibles / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of tangibles times closeadj
def tb_f38_tangible_book_pct_21d_base_v055_signal(tangibles, closeadj):
    result = _pct_change(tangibles, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of tangibles times closeadj
def tb_f38_tangible_book_pct_63d_base_v056_signal(tangibles, closeadj):
    result = _pct_change(tangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of tangibles times closeadj
def tb_f38_tangible_book_pct_252d_base_v057_signal(tangibles, closeadj):
    result = _pct_change(tangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of tangibles times closeadj
def tb_f38_tangible_book_sum_63d_base_v058_signal(tangibles, closeadj):
    result = tangibles.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of tangibles times closeadj
def tb_f38_tangible_book_sum_252d_base_v059_signal(tangibles, closeadj):
    result = tangibles.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of tangibles times closeadj
def tb_f38_tangible_book_sum_504d_base_v060_signal(tangibles, closeadj):
    result = tangibles.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed tangibles(63d) / smoothed assets(252d) x closeadj
def tb_f38_tangible_book_rom_assets_252_63d_base_v061_signal(tangibles, assets, closeadj):
    n = _mean(tangibles, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed tangibles(126d) / smoothed assets(504d) x closeadj
def tb_f38_tangible_book_rom_assets_504_126d_base_v062_signal(tangibles, assets, closeadj):
    n = _mean(tangibles, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed tangibles(63d) / smoothed marketcap(252d) x closeadj
def tb_f38_tangible_book_rom_marketcap_252_63d_base_v063_signal(tangibles, marketcap, closeadj):
    n = _mean(tangibles, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed tangibles(126d) / smoothed marketcap(504d) x closeadj
def tb_f38_tangible_book_rom_marketcap_504_126d_base_v064_signal(tangibles, marketcap, closeadj):
    n = _mean(tangibles, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed tangibles(63d) / smoothed equity(252d) x closeadj
def tb_f38_tangible_book_rom_equity_252_63d_base_v065_signal(tangibles, equity, closeadj):
    n = _mean(tangibles, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed tangibles(126d) / smoothed equity(504d) x closeadj
def tb_f38_tangible_book_rom_equity_504_126d_base_v066_signal(tangibles, equity, closeadj):
    n = _mean(tangibles, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(tangibles) / std(assets)
def tb_f38_tangible_book_volratio_assets_252d_base_v067_signal(tangibles, assets):
    n = _std(tangibles, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(tangibles) / std(assets)
def tb_f38_tangible_book_volratio_assets_504d_base_v068_signal(tangibles, assets):
    n = _std(tangibles, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(tangibles) / std(marketcap)
def tb_f38_tangible_book_volratio_marketcap_252d_base_v069_signal(tangibles, marketcap):
    n = _std(tangibles, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(tangibles) / std(marketcap)
def tb_f38_tangible_book_volratio_marketcap_504d_base_v070_signal(tangibles, marketcap):
    n = _std(tangibles, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed tangibles times closeadj
def tb_f38_tangible_book_raw_5d_base_v071_signal(tangibles, closeadj):
    result = _mean(tangibles, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed tangibles times closeadj
def tb_f38_tangible_book_raw_1008d_base_v072_signal(tangibles, closeadj):
    result = _mean(tangibles, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of tangibles/assets
def tb_f38_tangible_book_log_per_assets_252d_base_v073_signal(tangibles, assets):
    s = _tangible_book_scaled(tangibles, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of tangibles/assets
def tb_f38_tangible_book_log_per_assets_504d_base_v074_signal(tangibles, assets):
    s = _tangible_book_scaled(tangibles, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of tangibles/marketcap
def tb_f38_tangible_book_log_per_marketcap_252d_base_v075_signal(tangibles, marketcap):
    s = _tangible_book_scaled(tangibles, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
