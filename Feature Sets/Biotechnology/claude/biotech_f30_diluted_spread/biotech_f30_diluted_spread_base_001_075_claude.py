"""Family f30 - Basic vs diluted spread  (E_Dilution_Shares) | base 001-075"""
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
def _diluted_spread_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _diluted_spread_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _diluted_spread_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed shareswa times closeadj
def ds_f30_diluted_spread_raw_21d_base_v001_signal(shareswa, closeadj):
    result = _mean(shareswa, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed shareswa times closeadj
def ds_f30_diluted_spread_raw_63d_base_v002_signal(shareswa, closeadj):
    result = _mean(shareswa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed shareswa times closeadj
def ds_f30_diluted_spread_raw_126d_base_v003_signal(shareswa, closeadj):
    result = _mean(shareswa, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed shareswa times closeadj
def ds_f30_diluted_spread_raw_252d_base_v004_signal(shareswa, closeadj):
    result = _mean(shareswa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed shareswa times closeadj
def ds_f30_diluted_spread_raw_504d_base_v005_signal(shareswa, closeadj):
    result = _mean(shareswa, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(shareswa) times closeadj
def ds_f30_diluted_spread_log_21d_base_v006_signal(shareswa, closeadj):
    result = _mean(_diluted_spread_log(shareswa), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(shareswa) times closeadj
def ds_f30_diluted_spread_log_63d_base_v007_signal(shareswa, closeadj):
    result = _mean(_diluted_spread_log(shareswa), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(shareswa) times closeadj
def ds_f30_diluted_spread_log_126d_base_v008_signal(shareswa, closeadj):
    result = _mean(_diluted_spread_log(shareswa), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(shareswa) times closeadj
def ds_f30_diluted_spread_log_252d_base_v009_signal(shareswa, closeadj):
    result = _mean(_diluted_spread_log(shareswa), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(shareswa) times closeadj
def ds_f30_diluted_spread_log_504d_base_v010_signal(shareswa, closeadj):
    result = _mean(_diluted_spread_log(shareswa), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/assets mean
def ds_f30_diluted_spread_per_assets_63d_base_v011_signal(shareswa, assets):
    result = _mean(_diluted_spread_scaled(shareswa, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/assets mean
def ds_f30_diluted_spread_per_assets_252d_base_v012_signal(shareswa, assets):
    result = _mean(_diluted_spread_scaled(shareswa, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/assets mean
def ds_f30_diluted_spread_per_assets_504d_base_v013_signal(shareswa, assets):
    result = _mean(_diluted_spread_scaled(shareswa, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/marketcap mean
def ds_f30_diluted_spread_per_marketcap_63d_base_v014_signal(shareswa, marketcap):
    result = _mean(_diluted_spread_scaled(shareswa, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/marketcap mean
def ds_f30_diluted_spread_per_marketcap_252d_base_v015_signal(shareswa, marketcap):
    result = _mean(_diluted_spread_scaled(shareswa, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/marketcap mean
def ds_f30_diluted_spread_per_marketcap_504d_base_v016_signal(shareswa, marketcap):
    result = _mean(_diluted_spread_scaled(shareswa, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/equity mean
def ds_f30_diluted_spread_per_equity_63d_base_v017_signal(shareswa, equity):
    result = _mean(_diluted_spread_scaled(shareswa, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/equity mean
def ds_f30_diluted_spread_per_equity_252d_base_v018_signal(shareswa, equity):
    result = _mean(_diluted_spread_scaled(shareswa, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/equity mean
def ds_f30_diluted_spread_per_equity_504d_base_v019_signal(shareswa, equity):
    result = _mean(_diluted_spread_scaled(shareswa, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/debt mean
def ds_f30_diluted_spread_per_debt_63d_base_v020_signal(shareswa, debt):
    result = _mean(_diluted_spread_scaled(shareswa, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/debt mean
def ds_f30_diluted_spread_per_debt_252d_base_v021_signal(shareswa, debt):
    result = _mean(_diluted_spread_scaled(shareswa, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/debt mean
def ds_f30_diluted_spread_per_debt_504d_base_v022_signal(shareswa, debt):
    result = _mean(_diluted_spread_scaled(shareswa, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/revenue mean
def ds_f30_diluted_spread_per_revenue_63d_base_v023_signal(shareswa, revenue):
    result = _mean(_diluted_spread_scaled(shareswa, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/revenue mean
def ds_f30_diluted_spread_per_revenue_252d_base_v024_signal(shareswa, revenue):
    result = _mean(_diluted_spread_scaled(shareswa, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/revenue mean
def ds_f30_diluted_spread_per_revenue_504d_base_v025_signal(shareswa, revenue):
    result = _mean(_diluted_spread_scaled(shareswa, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d shareswa per share times closeadj
def ds_f30_diluted_spread_pershare_21d_base_v026_signal(shareswa, sharesbas, closeadj):
    ps = _diluted_spread_per_share(shareswa, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa per share times closeadj
def ds_f30_diluted_spread_pershare_63d_base_v027_signal(shareswa, sharesbas, closeadj):
    ps = _diluted_spread_per_share(shareswa, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d shareswa per share times closeadj
def ds_f30_diluted_spread_pershare_126d_base_v028_signal(shareswa, sharesbas, closeadj):
    ps = _diluted_spread_per_share(shareswa, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa per share times closeadj
def ds_f30_diluted_spread_pershare_252d_base_v029_signal(shareswa, sharesbas, closeadj):
    ps = _diluted_spread_per_share(shareswa, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa per share times closeadj
def ds_f30_diluted_spread_pershare_504d_base_v030_signal(shareswa, sharesbas, closeadj):
    ps = _diluted_spread_per_share(shareswa, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of shareswa times closeadj
def ds_f30_diluted_spread_std_63d_base_v031_signal(shareswa, closeadj):
    result = _std(shareswa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of shareswa times closeadj
def ds_f30_diluted_spread_std_252d_base_v032_signal(shareswa, closeadj):
    result = _std(shareswa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of shareswa times closeadj
def ds_f30_diluted_spread_std_504d_base_v033_signal(shareswa, closeadj):
    result = _std(shareswa, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of shareswa
def ds_f30_diluted_spread_z_252d_base_v034_signal(shareswa):
    result = _z(shareswa, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of shareswa
def ds_f30_diluted_spread_z_504d_base_v035_signal(shareswa):
    result = _z(shareswa, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(shareswa)
def ds_f30_diluted_spread_logz_252d_base_v036_signal(shareswa):
    result = _z(_diluted_spread_log(shareswa), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(shareswa)
def ds_f30_diluted_spread_logz_504d_base_v037_signal(shareswa):
    result = _z(_diluted_spread_log(shareswa), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of shareswa^2 times closeadj
def ds_f30_diluted_spread_sq_63d_base_v038_signal(shareswa, closeadj):
    result = _mean(shareswa * shareswa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of shareswa^2 times closeadj
def ds_f30_diluted_spread_sq_252d_base_v039_signal(shareswa, closeadj):
    result = _mean(shareswa * shareswa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(shareswa) times closeadj
def ds_f30_diluted_spread_sign_21d_base_v040_signal(shareswa, closeadj):
    result = _mean(np.sign(shareswa), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(shareswa) times closeadj
def ds_f30_diluted_spread_sign_63d_base_v041_signal(shareswa, closeadj):
    result = _mean(np.sign(shareswa), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(shareswa) times closeadj
def ds_f30_diluted_spread_sign_252d_base_v042_signal(shareswa, closeadj):
    result = _mean(np.sign(shareswa), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/opex mean
def ds_f30_diluted_spread_per_opex_63d_base_v043_signal(shareswa, opex):
    result = _mean(_diluted_spread_scaled(shareswa, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/opex mean
def ds_f30_diluted_spread_per_opex_252d_base_v044_signal(shareswa, opex):
    result = _mean(_diluted_spread_scaled(shareswa, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/ebitda mean
def ds_f30_diluted_spread_per_ebitda_63d_base_v045_signal(shareswa, ebitda):
    result = _mean(_diluted_spread_scaled(shareswa, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/ebitda mean
def ds_f30_diluted_spread_per_ebitda_252d_base_v046_signal(shareswa, ebitda):
    result = _mean(_diluted_spread_scaled(shareswa, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/capex mean
def ds_f30_diluted_spread_per_capex_63d_base_v047_signal(shareswa, capex):
    result = _mean(_diluted_spread_scaled(shareswa, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/capex mean
def ds_f30_diluted_spread_per_capex_252d_base_v048_signal(shareswa, capex):
    result = _mean(_diluted_spread_scaled(shareswa, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/liabilities mean
def ds_f30_diluted_spread_per_liabilities_63d_base_v049_signal(shareswa, liabilities):
    result = _mean(_diluted_spread_scaled(shareswa, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/liabilities mean
def ds_f30_diluted_spread_per_liabilities_252d_base_v050_signal(shareswa, liabilities):
    result = _mean(_diluted_spread_scaled(shareswa, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 252d max times closeadj
def ds_f30_diluted_spread_relmax_252d_base_v051_signal(shareswa, closeadj):
    peak = shareswa.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (shareswa / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 504d max times closeadj
def ds_f30_diluted_spread_relmax_504d_base_v052_signal(shareswa, closeadj):
    peak = shareswa.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (shareswa / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 252d min times closeadj
def ds_f30_diluted_spread_relmin_252d_base_v053_signal(shareswa, closeadj):
    trough = shareswa.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (shareswa / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 504d min times closeadj
def ds_f30_diluted_spread_relmin_504d_base_v054_signal(shareswa, closeadj):
    trough = shareswa.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (shareswa / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of shareswa times closeadj
def ds_f30_diluted_spread_pct_21d_base_v055_signal(shareswa, closeadj):
    result = _pct_change(shareswa, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of shareswa times closeadj
def ds_f30_diluted_spread_pct_63d_base_v056_signal(shareswa, closeadj):
    result = _pct_change(shareswa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of shareswa times closeadj
def ds_f30_diluted_spread_pct_252d_base_v057_signal(shareswa, closeadj):
    result = _pct_change(shareswa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of shareswa times closeadj
def ds_f30_diluted_spread_sum_63d_base_v058_signal(shareswa, closeadj):
    result = shareswa.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of shareswa times closeadj
def ds_f30_diluted_spread_sum_252d_base_v059_signal(shareswa, closeadj):
    result = shareswa.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of shareswa times closeadj
def ds_f30_diluted_spread_sum_504d_base_v060_signal(shareswa, closeadj):
    result = shareswa.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(63d) / smoothed assets(252d) x closeadj
def ds_f30_diluted_spread_rom_assets_252_63d_base_v061_signal(shareswa, assets, closeadj):
    n = _mean(shareswa, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(126d) / smoothed assets(504d) x closeadj
def ds_f30_diluted_spread_rom_assets_504_126d_base_v062_signal(shareswa, assets, closeadj):
    n = _mean(shareswa, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(63d) / smoothed marketcap(252d) x closeadj
def ds_f30_diluted_spread_rom_marketcap_252_63d_base_v063_signal(shareswa, marketcap, closeadj):
    n = _mean(shareswa, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(126d) / smoothed marketcap(504d) x closeadj
def ds_f30_diluted_spread_rom_marketcap_504_126d_base_v064_signal(shareswa, marketcap, closeadj):
    n = _mean(shareswa, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(63d) / smoothed equity(252d) x closeadj
def ds_f30_diluted_spread_rom_equity_252_63d_base_v065_signal(shareswa, equity, closeadj):
    n = _mean(shareswa, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(126d) / smoothed equity(504d) x closeadj
def ds_f30_diluted_spread_rom_equity_504_126d_base_v066_signal(shareswa, equity, closeadj):
    n = _mean(shareswa, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(shareswa) / std(assets)
def ds_f30_diluted_spread_volratio_assets_252d_base_v067_signal(shareswa, assets):
    n = _std(shareswa, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(shareswa) / std(assets)
def ds_f30_diluted_spread_volratio_assets_504d_base_v068_signal(shareswa, assets):
    n = _std(shareswa, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(shareswa) / std(marketcap)
def ds_f30_diluted_spread_volratio_marketcap_252d_base_v069_signal(shareswa, marketcap):
    n = _std(shareswa, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(shareswa) / std(marketcap)
def ds_f30_diluted_spread_volratio_marketcap_504d_base_v070_signal(shareswa, marketcap):
    n = _std(shareswa, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed shareswa times closeadj
def ds_f30_diluted_spread_raw_5d_base_v071_signal(shareswa, closeadj):
    result = _mean(shareswa, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed shareswa times closeadj
def ds_f30_diluted_spread_raw_1008d_base_v072_signal(shareswa, closeadj):
    result = _mean(shareswa, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of shareswa/assets
def ds_f30_diluted_spread_log_per_assets_252d_base_v073_signal(shareswa, assets):
    s = _diluted_spread_scaled(shareswa, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of shareswa/assets
def ds_f30_diluted_spread_log_per_assets_504d_base_v074_signal(shareswa, assets):
    s = _diluted_spread_scaled(shareswa, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of shareswa/marketcap
def ds_f30_diluted_spread_log_per_marketcap_252d_base_v075_signal(shareswa, marketcap):
    s = _diluted_spread_scaled(shareswa, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
