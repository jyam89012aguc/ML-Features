"""Family f061 - Tax assets and NOL proxy (Earnings and Quality) | Sharadar tables: SF1 | fields: taxassets, taxexp, ebt, assets | base 001-075"""
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
def _tax_asset_and_nol_proxy_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _tax_asset_and_nol_proxy_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _tax_asset_and_nol_proxy_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_raw_21d_base_v001_signal(taxassets, closeadj):
    result = _mean(taxassets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_raw_63d_base_v002_signal(taxassets, closeadj):
    result = _mean(taxassets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_raw_126d_base_v003_signal(taxassets, closeadj):
    result = _mean(taxassets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_raw_252d_base_v004_signal(taxassets, closeadj):
    result = _mean(taxassets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_raw_504d_base_v005_signal(taxassets, closeadj):
    result = _mean(taxassets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(taxassets) times closeadj
def taan_f061_tax_asset_and_nol_proxy_log_21d_base_v006_signal(taxassets, closeadj):
    result = _mean(_tax_asset_and_nol_proxy_log(taxassets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(taxassets) times closeadj
def taan_f061_tax_asset_and_nol_proxy_log_63d_base_v007_signal(taxassets, closeadj):
    result = _mean(_tax_asset_and_nol_proxy_log(taxassets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(taxassets) times closeadj
def taan_f061_tax_asset_and_nol_proxy_log_126d_base_v008_signal(taxassets, closeadj):
    result = _mean(_tax_asset_and_nol_proxy_log(taxassets), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(taxassets) times closeadj
def taan_f061_tax_asset_and_nol_proxy_log_252d_base_v009_signal(taxassets, closeadj):
    result = _mean(_tax_asset_and_nol_proxy_log(taxassets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(taxassets) times closeadj
def taan_f061_tax_asset_and_nol_proxy_log_504d_base_v010_signal(taxassets, closeadj):
    result = _mean(_tax_asset_and_nol_proxy_log(taxassets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets/taxexp mean
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_63d_base_v011_signal(taxassets, taxexp):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets/taxexp mean
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_252d_base_v012_signal(taxassets, taxexp):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxassets/taxexp mean
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_504d_base_v013_signal(taxassets, taxexp):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets/ebt mean
def taan_f061_tax_asset_and_nol_proxy_per_ebt_63d_base_v014_signal(taxassets, ebt):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets/ebt mean
def taan_f061_tax_asset_and_nol_proxy_per_ebt_252d_base_v015_signal(taxassets, ebt):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxassets/ebt mean
def taan_f061_tax_asset_and_nol_proxy_per_ebt_504d_base_v016_signal(taxassets, ebt):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets/assets mean
def taan_f061_tax_asset_and_nol_proxy_per_assets_63d_base_v017_signal(taxassets, assets):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets/assets mean
def taan_f061_tax_asset_and_nol_proxy_per_assets_252d_base_v018_signal(taxassets, assets):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxassets/assets mean
def taan_f061_tax_asset_and_nol_proxy_per_assets_504d_base_v019_signal(taxassets, assets):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets/marketcap mean
def taan_f061_tax_asset_and_nol_proxy_per_marketcap_63d_base_v020_signal(taxassets, marketcap):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets/marketcap mean
def taan_f061_tax_asset_and_nol_proxy_per_marketcap_252d_base_v021_signal(taxassets, marketcap):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxassets/marketcap mean
def taan_f061_tax_asset_and_nol_proxy_per_marketcap_504d_base_v022_signal(taxassets, marketcap):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets/equity mean
def taan_f061_tax_asset_and_nol_proxy_per_equity_63d_base_v023_signal(taxassets, equity):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets/equity mean
def taan_f061_tax_asset_and_nol_proxy_per_equity_252d_base_v024_signal(taxassets, equity):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxassets/equity mean
def taan_f061_tax_asset_and_nol_proxy_per_equity_504d_base_v025_signal(taxassets, equity):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d taxassets per share times closeadj
def taan_f061_tax_asset_and_nol_proxy_pershare_21d_base_v026_signal(taxassets, sharesbas, closeadj):
    ps = _tax_asset_and_nol_proxy_per_share(taxassets, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets per share times closeadj
def taan_f061_tax_asset_and_nol_proxy_pershare_63d_base_v027_signal(taxassets, sharesbas, closeadj):
    ps = _tax_asset_and_nol_proxy_per_share(taxassets, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d taxassets per share times closeadj
def taan_f061_tax_asset_and_nol_proxy_pershare_126d_base_v028_signal(taxassets, sharesbas, closeadj):
    ps = _tax_asset_and_nol_proxy_per_share(taxassets, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets per share times closeadj
def taan_f061_tax_asset_and_nol_proxy_pershare_252d_base_v029_signal(taxassets, sharesbas, closeadj):
    ps = _tax_asset_and_nol_proxy_per_share(taxassets, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxassets per share times closeadj
def taan_f061_tax_asset_and_nol_proxy_pershare_504d_base_v030_signal(taxassets, sharesbas, closeadj):
    ps = _tax_asset_and_nol_proxy_per_share(taxassets, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_std_63d_base_v031_signal(taxassets, closeadj):
    result = _std(taxassets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_std_252d_base_v032_signal(taxassets, closeadj):
    result = _std(taxassets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_std_504d_base_v033_signal(taxassets, closeadj):
    result = _std(taxassets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of taxassets
def taan_f061_tax_asset_and_nol_proxy_z_252d_base_v034_signal(taxassets):
    result = _z(taxassets, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of taxassets
def taan_f061_tax_asset_and_nol_proxy_z_504d_base_v035_signal(taxassets):
    result = _z(taxassets, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(taxassets)
def taan_f061_tax_asset_and_nol_proxy_logz_252d_base_v036_signal(taxassets):
    result = _z(_tax_asset_and_nol_proxy_log(taxassets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(taxassets)
def taan_f061_tax_asset_and_nol_proxy_logz_504d_base_v037_signal(taxassets):
    result = _z(_tax_asset_and_nol_proxy_log(taxassets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of taxassets^2 times closeadj
def taan_f061_tax_asset_and_nol_proxy_sq_63d_base_v038_signal(taxassets, closeadj):
    result = _mean(taxassets * taxassets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of taxassets^2 times closeadj
def taan_f061_tax_asset_and_nol_proxy_sq_252d_base_v039_signal(taxassets, closeadj):
    result = _mean(taxassets * taxassets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(taxassets) times closeadj
def taan_f061_tax_asset_and_nol_proxy_sign_21d_base_v040_signal(taxassets, closeadj):
    result = _mean(np.sign(taxassets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(taxassets) times closeadj
def taan_f061_tax_asset_and_nol_proxy_sign_63d_base_v041_signal(taxassets, closeadj):
    result = _mean(np.sign(taxassets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(taxassets) times closeadj
def taan_f061_tax_asset_and_nol_proxy_sign_252d_base_v042_signal(taxassets, closeadj):
    result = _mean(np.sign(taxassets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets/opex mean
def taan_f061_tax_asset_and_nol_proxy_per_opex_63d_base_v043_signal(taxassets, opex):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets/opex mean
def taan_f061_tax_asset_and_nol_proxy_per_opex_252d_base_v044_signal(taxassets, opex):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets/ebitda mean
def taan_f061_tax_asset_and_nol_proxy_per_ebitda_63d_base_v045_signal(taxassets, ebitda):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets/ebitda mean
def taan_f061_tax_asset_and_nol_proxy_per_ebitda_252d_base_v046_signal(taxassets, ebitda):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets/capex mean
def taan_f061_tax_asset_and_nol_proxy_per_capex_63d_base_v047_signal(taxassets, capex):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets/capex mean
def taan_f061_tax_asset_and_nol_proxy_per_capex_252d_base_v048_signal(taxassets, capex):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxassets/liabilities mean
def taan_f061_tax_asset_and_nol_proxy_per_liabilities_63d_base_v049_signal(taxassets, liabilities):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxassets/liabilities mean
def taan_f061_tax_asset_and_nol_proxy_per_liabilities_252d_base_v050_signal(taxassets, liabilities):
    result = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# taxassets relative to 252d max times closeadj
def taan_f061_tax_asset_and_nol_proxy_relmax_252d_base_v051_signal(taxassets, closeadj):
    peak = taxassets.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (taxassets / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# taxassets relative to 504d max times closeadj
def taan_f061_tax_asset_and_nol_proxy_relmax_504d_base_v052_signal(taxassets, closeadj):
    peak = taxassets.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (taxassets / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# taxassets relative to 252d min times closeadj
def taan_f061_tax_asset_and_nol_proxy_relmin_252d_base_v053_signal(taxassets, closeadj):
    trough = taxassets.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (taxassets / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# taxassets relative to 504d min times closeadj
def taan_f061_tax_asset_and_nol_proxy_relmin_504d_base_v054_signal(taxassets, closeadj):
    trough = taxassets.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (taxassets / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_pct_21d_base_v055_signal(taxassets, closeadj):
    result = _pct_change(taxassets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_pct_63d_base_v056_signal(taxassets, closeadj):
    result = _pct_change(taxassets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_pct_252d_base_v057_signal(taxassets, closeadj):
    result = _pct_change(taxassets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_sum_63d_base_v058_signal(taxassets, closeadj):
    result = taxassets.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_sum_252d_base_v059_signal(taxassets, closeadj):
    result = taxassets.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_sum_504d_base_v060_signal(taxassets, closeadj):
    result = taxassets.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxassets(63d) / smoothed taxexp(252d) x closeadj
def taan_f061_tax_asset_and_nol_proxy_rom_taxexp_252_63d_base_v061_signal(taxassets, taxexp, closeadj):
    n = _mean(taxassets, 63)
    d = _mean(taxexp, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxassets(126d) / smoothed taxexp(504d) x closeadj
def taan_f061_tax_asset_and_nol_proxy_rom_taxexp_504_126d_base_v062_signal(taxassets, taxexp, closeadj):
    n = _mean(taxassets, 126)
    d = _mean(taxexp, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxassets(63d) / smoothed ebt(252d) x closeadj
def taan_f061_tax_asset_and_nol_proxy_rom_ebt_252_63d_base_v063_signal(taxassets, ebt, closeadj):
    n = _mean(taxassets, 63)
    d = _mean(ebt, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxassets(126d) / smoothed ebt(504d) x closeadj
def taan_f061_tax_asset_and_nol_proxy_rom_ebt_504_126d_base_v064_signal(taxassets, ebt, closeadj):
    n = _mean(taxassets, 126)
    d = _mean(ebt, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxassets(63d) / smoothed assets(252d) x closeadj
def taan_f061_tax_asset_and_nol_proxy_rom_assets_252_63d_base_v065_signal(taxassets, assets, closeadj):
    n = _mean(taxassets, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxassets(126d) / smoothed assets(504d) x closeadj
def taan_f061_tax_asset_and_nol_proxy_rom_assets_504_126d_base_v066_signal(taxassets, assets, closeadj):
    n = _mean(taxassets, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(taxassets) / std(taxexp)
def taan_f061_tax_asset_and_nol_proxy_volratio_taxexp_252d_base_v067_signal(taxassets, taxexp):
    n = _std(taxassets, 252)
    d = _std(taxexp, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(taxassets) / std(taxexp)
def taan_f061_tax_asset_and_nol_proxy_volratio_taxexp_504d_base_v068_signal(taxassets, taxexp):
    n = _std(taxassets, 504)
    d = _std(taxexp, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(taxassets) / std(ebt)
def taan_f061_tax_asset_and_nol_proxy_volratio_ebt_252d_base_v069_signal(taxassets, ebt):
    n = _std(taxassets, 252)
    d = _std(ebt, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(taxassets) / std(ebt)
def taan_f061_tax_asset_and_nol_proxy_volratio_ebt_504d_base_v070_signal(taxassets, ebt):
    n = _std(taxassets, 504)
    d = _std(ebt, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_raw_5d_base_v071_signal(taxassets, closeadj):
    result = _mean(taxassets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_raw_1008d_base_v072_signal(taxassets, closeadj):
    result = _mean(taxassets, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of taxassets/taxexp
def taan_f061_tax_asset_and_nol_proxy_log_per_taxexp_252d_base_v073_signal(taxassets, taxexp):
    s = _tax_asset_and_nol_proxy_scaled(taxassets, taxexp)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of taxassets/taxexp
def taan_f061_tax_asset_and_nol_proxy_log_per_taxexp_504d_base_v074_signal(taxassets, taxexp):
    s = _tax_asset_and_nol_proxy_scaled(taxassets, taxexp)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of taxassets/ebt
def taan_f061_tax_asset_and_nol_proxy_log_per_ebt_252d_base_v075_signal(taxassets, ebt):
    s = _tax_asset_and_nol_proxy_scaled(taxassets, ebt)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
