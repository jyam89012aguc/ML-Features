"""Family f032 - Diluted share overhang (Dilution and Share Count) | Sharadar tables: SF1 | fields: shareswa, shareswadil, sharesbas | base 001-075"""
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
def _shares_diluted_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _shares_diluted_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _shares_diluted_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed shareswa times closeadj
def sd_f032_shares_diluted_raw_21d_base_v001_signal(shareswa, closeadj):
    result = _mean(shareswa, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed shareswa times closeadj
def sd_f032_shares_diluted_raw_63d_base_v002_signal(shareswa, closeadj):
    result = _mean(shareswa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed shareswa times closeadj
def sd_f032_shares_diluted_raw_126d_base_v003_signal(shareswa, closeadj):
    result = _mean(shareswa, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed shareswa times closeadj
def sd_f032_shares_diluted_raw_252d_base_v004_signal(shareswa, closeadj):
    result = _mean(shareswa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed shareswa times closeadj
def sd_f032_shares_diluted_raw_504d_base_v005_signal(shareswa, closeadj):
    result = _mean(shareswa, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(shareswa) times closeadj
def sd_f032_shares_diluted_log_21d_base_v006_signal(shareswa, closeadj):
    result = _mean(_shares_diluted_log(shareswa), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(shareswa) times closeadj
def sd_f032_shares_diluted_log_63d_base_v007_signal(shareswa, closeadj):
    result = _mean(_shares_diluted_log(shareswa), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(shareswa) times closeadj
def sd_f032_shares_diluted_log_126d_base_v008_signal(shareswa, closeadj):
    result = _mean(_shares_diluted_log(shareswa), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(shareswa) times closeadj
def sd_f032_shares_diluted_log_252d_base_v009_signal(shareswa, closeadj):
    result = _mean(_shares_diluted_log(shareswa), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(shareswa) times closeadj
def sd_f032_shares_diluted_log_504d_base_v010_signal(shareswa, closeadj):
    result = _mean(_shares_diluted_log(shareswa), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/shareswadil mean
def sd_f032_shares_diluted_per_shareswadil_63d_base_v011_signal(shareswa, shareswadil):
    result = _mean(_shares_diluted_scaled(shareswa, shareswadil), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/shareswadil mean
def sd_f032_shares_diluted_per_shareswadil_252d_base_v012_signal(shareswa, shareswadil):
    result = _mean(_shares_diluted_scaled(shareswa, shareswadil), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/shareswadil mean
def sd_f032_shares_diluted_per_shareswadil_504d_base_v013_signal(shareswa, shareswadil):
    result = _mean(_shares_diluted_scaled(shareswa, shareswadil), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/sharesbas mean
def sd_f032_shares_diluted_per_sharesbas_63d_base_v014_signal(shareswa, sharesbas):
    result = _mean(_shares_diluted_scaled(shareswa, sharesbas), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/sharesbas mean
def sd_f032_shares_diluted_per_sharesbas_252d_base_v015_signal(shareswa, sharesbas):
    result = _mean(_shares_diluted_scaled(shareswa, sharesbas), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/sharesbas mean
def sd_f032_shares_diluted_per_sharesbas_504d_base_v016_signal(shareswa, sharesbas):
    result = _mean(_shares_diluted_scaled(shareswa, sharesbas), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/assets mean
def sd_f032_shares_diluted_per_assets_63d_base_v017_signal(shareswa, assets):
    result = _mean(_shares_diluted_scaled(shareswa, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/assets mean
def sd_f032_shares_diluted_per_assets_252d_base_v018_signal(shareswa, assets):
    result = _mean(_shares_diluted_scaled(shareswa, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/assets mean
def sd_f032_shares_diluted_per_assets_504d_base_v019_signal(shareswa, assets):
    result = _mean(_shares_diluted_scaled(shareswa, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/marketcap mean
def sd_f032_shares_diluted_per_marketcap_63d_base_v020_signal(shareswa, marketcap):
    result = _mean(_shares_diluted_scaled(shareswa, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/marketcap mean
def sd_f032_shares_diluted_per_marketcap_252d_base_v021_signal(shareswa, marketcap):
    result = _mean(_shares_diluted_scaled(shareswa, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/marketcap mean
def sd_f032_shares_diluted_per_marketcap_504d_base_v022_signal(shareswa, marketcap):
    result = _mean(_shares_diluted_scaled(shareswa, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/equity mean
def sd_f032_shares_diluted_per_equity_63d_base_v023_signal(shareswa, equity):
    result = _mean(_shares_diluted_scaled(shareswa, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/equity mean
def sd_f032_shares_diluted_per_equity_252d_base_v024_signal(shareswa, equity):
    result = _mean(_shares_diluted_scaled(shareswa, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa/equity mean
def sd_f032_shares_diluted_per_equity_504d_base_v025_signal(shareswa, equity):
    result = _mean(_shares_diluted_scaled(shareswa, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d shareswa per share times closeadj
def sd_f032_shares_diluted_pershare_21d_base_v026_signal(shareswa, sharesbas, closeadj):
    ps = _shares_diluted_per_share(shareswa, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa per share times closeadj
def sd_f032_shares_diluted_pershare_63d_base_v027_signal(shareswa, sharesbas, closeadj):
    ps = _shares_diluted_per_share(shareswa, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d shareswa per share times closeadj
def sd_f032_shares_diluted_pershare_126d_base_v028_signal(shareswa, sharesbas, closeadj):
    ps = _shares_diluted_per_share(shareswa, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa per share times closeadj
def sd_f032_shares_diluted_pershare_252d_base_v029_signal(shareswa, sharesbas, closeadj):
    ps = _shares_diluted_per_share(shareswa, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa per share times closeadj
def sd_f032_shares_diluted_pershare_504d_base_v030_signal(shareswa, sharesbas, closeadj):
    ps = _shares_diluted_per_share(shareswa, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of shareswa times closeadj
def sd_f032_shares_diluted_std_63d_base_v031_signal(shareswa, closeadj):
    result = _std(shareswa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of shareswa times closeadj
def sd_f032_shares_diluted_std_252d_base_v032_signal(shareswa, closeadj):
    result = _std(shareswa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of shareswa times closeadj
def sd_f032_shares_diluted_std_504d_base_v033_signal(shareswa, closeadj):
    result = _std(shareswa, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of shareswa
def sd_f032_shares_diluted_z_252d_base_v034_signal(shareswa):
    result = _z(shareswa, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of shareswa
def sd_f032_shares_diluted_z_504d_base_v035_signal(shareswa):
    result = _z(shareswa, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(shareswa)
def sd_f032_shares_diluted_logz_252d_base_v036_signal(shareswa):
    result = _z(_shares_diluted_log(shareswa), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(shareswa)
def sd_f032_shares_diluted_logz_504d_base_v037_signal(shareswa):
    result = _z(_shares_diluted_log(shareswa), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of shareswa^2 times closeadj
def sd_f032_shares_diluted_sq_63d_base_v038_signal(shareswa, closeadj):
    result = _mean(shareswa * shareswa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of shareswa^2 times closeadj
def sd_f032_shares_diluted_sq_252d_base_v039_signal(shareswa, closeadj):
    result = _mean(shareswa * shareswa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(shareswa) times closeadj
def sd_f032_shares_diluted_sign_21d_base_v040_signal(shareswa, closeadj):
    result = _mean(np.sign(shareswa), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(shareswa) times closeadj
def sd_f032_shares_diluted_sign_63d_base_v041_signal(shareswa, closeadj):
    result = _mean(np.sign(shareswa), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(shareswa) times closeadj
def sd_f032_shares_diluted_sign_252d_base_v042_signal(shareswa, closeadj):
    result = _mean(np.sign(shareswa), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/opex mean
def sd_f032_shares_diluted_per_opex_63d_base_v043_signal(shareswa, opex):
    result = _mean(_shares_diluted_scaled(shareswa, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/opex mean
def sd_f032_shares_diluted_per_opex_252d_base_v044_signal(shareswa, opex):
    result = _mean(_shares_diluted_scaled(shareswa, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/ebitda mean
def sd_f032_shares_diluted_per_ebitda_63d_base_v045_signal(shareswa, ebitda):
    result = _mean(_shares_diluted_scaled(shareswa, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/ebitda mean
def sd_f032_shares_diluted_per_ebitda_252d_base_v046_signal(shareswa, ebitda):
    result = _mean(_shares_diluted_scaled(shareswa, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/capex mean
def sd_f032_shares_diluted_per_capex_63d_base_v047_signal(shareswa, capex):
    result = _mean(_shares_diluted_scaled(shareswa, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/capex mean
def sd_f032_shares_diluted_per_capex_252d_base_v048_signal(shareswa, capex):
    result = _mean(_shares_diluted_scaled(shareswa, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa/liabilities mean
def sd_f032_shares_diluted_per_liabilities_63d_base_v049_signal(shareswa, liabilities):
    result = _mean(_shares_diluted_scaled(shareswa, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa/liabilities mean
def sd_f032_shares_diluted_per_liabilities_252d_base_v050_signal(shareswa, liabilities):
    result = _mean(_shares_diluted_scaled(shareswa, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 252d max times closeadj
def sd_f032_shares_diluted_relmax_252d_base_v051_signal(shareswa, closeadj):
    peak = shareswa.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (shareswa / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 504d max times closeadj
def sd_f032_shares_diluted_relmax_504d_base_v052_signal(shareswa, closeadj):
    peak = shareswa.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (shareswa / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 252d min times closeadj
def sd_f032_shares_diluted_relmin_252d_base_v053_signal(shareswa, closeadj):
    trough = shareswa.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (shareswa / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 504d min times closeadj
def sd_f032_shares_diluted_relmin_504d_base_v054_signal(shareswa, closeadj):
    trough = shareswa.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (shareswa / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of shareswa times closeadj
def sd_f032_shares_diluted_pct_21d_base_v055_signal(shareswa, closeadj):
    result = _pct_change(shareswa, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of shareswa times closeadj
def sd_f032_shares_diluted_pct_63d_base_v056_signal(shareswa, closeadj):
    result = _pct_change(shareswa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of shareswa times closeadj
def sd_f032_shares_diluted_pct_252d_base_v057_signal(shareswa, closeadj):
    result = _pct_change(shareswa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of shareswa times closeadj
def sd_f032_shares_diluted_sum_63d_base_v058_signal(shareswa, closeadj):
    result = shareswa.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of shareswa times closeadj
def sd_f032_shares_diluted_sum_252d_base_v059_signal(shareswa, closeadj):
    result = shareswa.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of shareswa times closeadj
def sd_f032_shares_diluted_sum_504d_base_v060_signal(shareswa, closeadj):
    result = shareswa.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(63d) / smoothed shareswadil(252d) x closeadj
def sd_f032_shares_diluted_rom_shareswadil_252_63d_base_v061_signal(shareswa, shareswadil, closeadj):
    n = _mean(shareswa, 63)
    d = _mean(shareswadil, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(126d) / smoothed shareswadil(504d) x closeadj
def sd_f032_shares_diluted_rom_shareswadil_504_126d_base_v062_signal(shareswa, shareswadil, closeadj):
    n = _mean(shareswa, 126)
    d = _mean(shareswadil, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(63d) / smoothed sharesbas(252d) x closeadj
def sd_f032_shares_diluted_rom_sharesbas_252_63d_base_v063_signal(shareswa, sharesbas, closeadj):
    n = _mean(shareswa, 63)
    d = _mean(sharesbas, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(126d) / smoothed sharesbas(504d) x closeadj
def sd_f032_shares_diluted_rom_sharesbas_504_126d_base_v064_signal(shareswa, sharesbas, closeadj):
    n = _mean(shareswa, 126)
    d = _mean(sharesbas, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(63d) / smoothed assets(252d) x closeadj
def sd_f032_shares_diluted_rom_assets_252_63d_base_v065_signal(shareswa, assets, closeadj):
    n = _mean(shareswa, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed shareswa(126d) / smoothed assets(504d) x closeadj
def sd_f032_shares_diluted_rom_assets_504_126d_base_v066_signal(shareswa, assets, closeadj):
    n = _mean(shareswa, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(shareswa) / std(shareswadil)
def sd_f032_shares_diluted_volratio_shareswadil_252d_base_v067_signal(shareswa, shareswadil):
    n = _std(shareswa, 252)
    d = _std(shareswadil, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(shareswa) / std(shareswadil)
def sd_f032_shares_diluted_volratio_shareswadil_504d_base_v068_signal(shareswa, shareswadil):
    n = _std(shareswa, 504)
    d = _std(shareswadil, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(shareswa) / std(sharesbas)
def sd_f032_shares_diluted_volratio_sharesbas_252d_base_v069_signal(shareswa, sharesbas):
    n = _std(shareswa, 252)
    d = _std(sharesbas, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(shareswa) / std(sharesbas)
def sd_f032_shares_diluted_volratio_sharesbas_504d_base_v070_signal(shareswa, sharesbas):
    n = _std(shareswa, 504)
    d = _std(sharesbas, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed shareswa times closeadj
def sd_f032_shares_diluted_raw_5d_base_v071_signal(shareswa, closeadj):
    result = _mean(shareswa, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed shareswa times closeadj
def sd_f032_shares_diluted_raw_1008d_base_v072_signal(shareswa, closeadj):
    result = _mean(shareswa, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of shareswa/shareswadil
def sd_f032_shares_diluted_log_per_shareswadil_252d_base_v073_signal(shareswa, shareswadil):
    s = _shares_diluted_scaled(shareswa, shareswadil)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of shareswa/shareswadil
def sd_f032_shares_diluted_log_per_shareswadil_504d_base_v074_signal(shareswa, shareswadil):
    s = _shares_diluted_scaled(shareswa, shareswadil)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of shareswa/sharesbas
def sd_f032_shares_diluted_log_per_sharesbas_252d_base_v075_signal(shareswa, sharesbas):
    s = _shares_diluted_scaled(shareswa, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
