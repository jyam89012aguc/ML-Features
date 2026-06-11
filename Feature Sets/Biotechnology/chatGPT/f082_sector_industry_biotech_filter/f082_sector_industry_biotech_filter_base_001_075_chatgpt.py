"""Family f082 - Sector and industry biotech filter (Security Master and Universe) | Sharadar tables: TICKERS | fields: sector, industry, sicsector, sicindustry, famasector, famaindustry | base 001-075"""
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
def _sector_industry_biotech_filter_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sector_industry_biotech_filter_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sector_industry_biotech_filter_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_raw_21d_base_v001_signal(sector_rank, closeadj):
    result = _mean(sector_rank, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_raw_63d_base_v002_signal(sector_rank, closeadj):
    result = _mean(sector_rank, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_raw_126d_base_v003_signal(sector_rank, closeadj):
    result = _mean(sector_rank, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_raw_252d_base_v004_signal(sector_rank, closeadj):
    result = _mean(sector_rank, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_raw_504d_base_v005_signal(sector_rank, closeadj):
    result = _mean(sector_rank, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(sector_rank) times closeadj
def sibf_f082_sector_industry_biotech_filter_log_21d_base_v006_signal(sector_rank, closeadj):
    result = _mean(_sector_industry_biotech_filter_log(sector_rank), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(sector_rank) times closeadj
def sibf_f082_sector_industry_biotech_filter_log_63d_base_v007_signal(sector_rank, closeadj):
    result = _mean(_sector_industry_biotech_filter_log(sector_rank), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(sector_rank) times closeadj
def sibf_f082_sector_industry_biotech_filter_log_126d_base_v008_signal(sector_rank, closeadj):
    result = _mean(_sector_industry_biotech_filter_log(sector_rank), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(sector_rank) times closeadj
def sibf_f082_sector_industry_biotech_filter_log_252d_base_v009_signal(sector_rank, closeadj):
    result = _mean(_sector_industry_biotech_filter_log(sector_rank), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(sector_rank) times closeadj
def sibf_f082_sector_industry_biotech_filter_log_504d_base_v010_signal(sector_rank, closeadj):
    result = _mean(_sector_industry_biotech_filter_log(sector_rank), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank/assets mean
def sibf_f082_sector_industry_biotech_filter_per_assets_63d_base_v011_signal(sector_rank, assets):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank/assets mean
def sibf_f082_sector_industry_biotech_filter_per_assets_252d_base_v012_signal(sector_rank, assets):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sector_rank/assets mean
def sibf_f082_sector_industry_biotech_filter_per_assets_504d_base_v013_signal(sector_rank, assets):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank/marketcap mean
def sibf_f082_sector_industry_biotech_filter_per_marketcap_63d_base_v014_signal(sector_rank, marketcap):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank/marketcap mean
def sibf_f082_sector_industry_biotech_filter_per_marketcap_252d_base_v015_signal(sector_rank, marketcap):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sector_rank/marketcap mean
def sibf_f082_sector_industry_biotech_filter_per_marketcap_504d_base_v016_signal(sector_rank, marketcap):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank/equity mean
def sibf_f082_sector_industry_biotech_filter_per_equity_63d_base_v017_signal(sector_rank, equity):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank/equity mean
def sibf_f082_sector_industry_biotech_filter_per_equity_252d_base_v018_signal(sector_rank, equity):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sector_rank/equity mean
def sibf_f082_sector_industry_biotech_filter_per_equity_504d_base_v019_signal(sector_rank, equity):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank/debt mean
def sibf_f082_sector_industry_biotech_filter_per_debt_63d_base_v020_signal(sector_rank, debt):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank/debt mean
def sibf_f082_sector_industry_biotech_filter_per_debt_252d_base_v021_signal(sector_rank, debt):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sector_rank/debt mean
def sibf_f082_sector_industry_biotech_filter_per_debt_504d_base_v022_signal(sector_rank, debt):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank/revenue mean
def sibf_f082_sector_industry_biotech_filter_per_revenue_63d_base_v023_signal(sector_rank, revenue):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank/revenue mean
def sibf_f082_sector_industry_biotech_filter_per_revenue_252d_base_v024_signal(sector_rank, revenue):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sector_rank/revenue mean
def sibf_f082_sector_industry_biotech_filter_per_revenue_504d_base_v025_signal(sector_rank, revenue):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sector_rank per share times closeadj
def sibf_f082_sector_industry_biotech_filter_pershare_21d_base_v026_signal(sector_rank, sharesbas, closeadj):
    ps = _sector_industry_biotech_filter_per_share(sector_rank, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank per share times closeadj
def sibf_f082_sector_industry_biotech_filter_pershare_63d_base_v027_signal(sector_rank, sharesbas, closeadj):
    ps = _sector_industry_biotech_filter_per_share(sector_rank, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sector_rank per share times closeadj
def sibf_f082_sector_industry_biotech_filter_pershare_126d_base_v028_signal(sector_rank, sharesbas, closeadj):
    ps = _sector_industry_biotech_filter_per_share(sector_rank, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank per share times closeadj
def sibf_f082_sector_industry_biotech_filter_pershare_252d_base_v029_signal(sector_rank, sharesbas, closeadj):
    ps = _sector_industry_biotech_filter_per_share(sector_rank, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sector_rank per share times closeadj
def sibf_f082_sector_industry_biotech_filter_pershare_504d_base_v030_signal(sector_rank, sharesbas, closeadj):
    ps = _sector_industry_biotech_filter_per_share(sector_rank, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_std_63d_base_v031_signal(sector_rank, closeadj):
    result = _std(sector_rank, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_std_252d_base_v032_signal(sector_rank, closeadj):
    result = _std(sector_rank, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_std_504d_base_v033_signal(sector_rank, closeadj):
    result = _std(sector_rank, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of sector_rank
def sibf_f082_sector_industry_biotech_filter_z_252d_base_v034_signal(sector_rank):
    result = _z(sector_rank, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of sector_rank
def sibf_f082_sector_industry_biotech_filter_z_504d_base_v035_signal(sector_rank):
    result = _z(sector_rank, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(sector_rank)
def sibf_f082_sector_industry_biotech_filter_logz_252d_base_v036_signal(sector_rank):
    result = _z(_sector_industry_biotech_filter_log(sector_rank), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(sector_rank)
def sibf_f082_sector_industry_biotech_filter_logz_504d_base_v037_signal(sector_rank):
    result = _z(_sector_industry_biotech_filter_log(sector_rank), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sector_rank^2 times closeadj
def sibf_f082_sector_industry_biotech_filter_sq_63d_base_v038_signal(sector_rank, closeadj):
    result = _mean(sector_rank * sector_rank, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sector_rank^2 times closeadj
def sibf_f082_sector_industry_biotech_filter_sq_252d_base_v039_signal(sector_rank, closeadj):
    result = _mean(sector_rank * sector_rank, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(sector_rank) times closeadj
def sibf_f082_sector_industry_biotech_filter_sign_21d_base_v040_signal(sector_rank, closeadj):
    result = _mean(np.sign(sector_rank), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(sector_rank) times closeadj
def sibf_f082_sector_industry_biotech_filter_sign_63d_base_v041_signal(sector_rank, closeadj):
    result = _mean(np.sign(sector_rank), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(sector_rank) times closeadj
def sibf_f082_sector_industry_biotech_filter_sign_252d_base_v042_signal(sector_rank, closeadj):
    result = _mean(np.sign(sector_rank), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank/opex mean
def sibf_f082_sector_industry_biotech_filter_per_opex_63d_base_v043_signal(sector_rank, opex):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank/opex mean
def sibf_f082_sector_industry_biotech_filter_per_opex_252d_base_v044_signal(sector_rank, opex):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank/ebitda mean
def sibf_f082_sector_industry_biotech_filter_per_ebitda_63d_base_v045_signal(sector_rank, ebitda):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank/ebitda mean
def sibf_f082_sector_industry_biotech_filter_per_ebitda_252d_base_v046_signal(sector_rank, ebitda):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank/capex mean
def sibf_f082_sector_industry_biotech_filter_per_capex_63d_base_v047_signal(sector_rank, capex):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank/capex mean
def sibf_f082_sector_industry_biotech_filter_per_capex_252d_base_v048_signal(sector_rank, capex):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sector_rank/liabilities mean
def sibf_f082_sector_industry_biotech_filter_per_liabilities_63d_base_v049_signal(sector_rank, liabilities):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sector_rank/liabilities mean
def sibf_f082_sector_industry_biotech_filter_per_liabilities_252d_base_v050_signal(sector_rank, liabilities):
    result = _mean(_sector_industry_biotech_filter_scaled(sector_rank, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sector_rank relative to 252d max times closeadj
def sibf_f082_sector_industry_biotech_filter_relmax_252d_base_v051_signal(sector_rank, closeadj):
    peak = sector_rank.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (sector_rank / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sector_rank relative to 504d max times closeadj
def sibf_f082_sector_industry_biotech_filter_relmax_504d_base_v052_signal(sector_rank, closeadj):
    peak = sector_rank.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (sector_rank / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sector_rank relative to 252d min times closeadj
def sibf_f082_sector_industry_biotech_filter_relmin_252d_base_v053_signal(sector_rank, closeadj):
    trough = sector_rank.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (sector_rank / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sector_rank relative to 504d min times closeadj
def sibf_f082_sector_industry_biotech_filter_relmin_504d_base_v054_signal(sector_rank, closeadj):
    trough = sector_rank.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (sector_rank / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_pct_21d_base_v055_signal(sector_rank, closeadj):
    result = _pct_change(sector_rank, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_pct_63d_base_v056_signal(sector_rank, closeadj):
    result = _pct_change(sector_rank, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_pct_252d_base_v057_signal(sector_rank, closeadj):
    result = _pct_change(sector_rank, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_sum_63d_base_v058_signal(sector_rank, closeadj):
    result = sector_rank.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_sum_252d_base_v059_signal(sector_rank, closeadj):
    result = sector_rank.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_sum_504d_base_v060_signal(sector_rank, closeadj):
    result = sector_rank.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sector_rank(63d) / smoothed assets(252d) x closeadj
def sibf_f082_sector_industry_biotech_filter_rom_assets_252_63d_base_v061_signal(sector_rank, assets, closeadj):
    n = _mean(sector_rank, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sector_rank(126d) / smoothed assets(504d) x closeadj
def sibf_f082_sector_industry_biotech_filter_rom_assets_504_126d_base_v062_signal(sector_rank, assets, closeadj):
    n = _mean(sector_rank, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sector_rank(63d) / smoothed marketcap(252d) x closeadj
def sibf_f082_sector_industry_biotech_filter_rom_marketcap_252_63d_base_v063_signal(sector_rank, marketcap, closeadj):
    n = _mean(sector_rank, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sector_rank(126d) / smoothed marketcap(504d) x closeadj
def sibf_f082_sector_industry_biotech_filter_rom_marketcap_504_126d_base_v064_signal(sector_rank, marketcap, closeadj):
    n = _mean(sector_rank, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sector_rank(63d) / smoothed equity(252d) x closeadj
def sibf_f082_sector_industry_biotech_filter_rom_equity_252_63d_base_v065_signal(sector_rank, equity, closeadj):
    n = _mean(sector_rank, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sector_rank(126d) / smoothed equity(504d) x closeadj
def sibf_f082_sector_industry_biotech_filter_rom_equity_504_126d_base_v066_signal(sector_rank, equity, closeadj):
    n = _mean(sector_rank, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sector_rank) / std(assets)
def sibf_f082_sector_industry_biotech_filter_volratio_assets_252d_base_v067_signal(sector_rank, assets):
    n = _std(sector_rank, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sector_rank) / std(assets)
def sibf_f082_sector_industry_biotech_filter_volratio_assets_504d_base_v068_signal(sector_rank, assets):
    n = _std(sector_rank, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sector_rank) / std(marketcap)
def sibf_f082_sector_industry_biotech_filter_volratio_marketcap_252d_base_v069_signal(sector_rank, marketcap):
    n = _std(sector_rank, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sector_rank) / std(marketcap)
def sibf_f082_sector_industry_biotech_filter_volratio_marketcap_504d_base_v070_signal(sector_rank, marketcap):
    n = _std(sector_rank, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_raw_5d_base_v071_signal(sector_rank, closeadj):
    result = _mean(sector_rank, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_raw_1008d_base_v072_signal(sector_rank, closeadj):
    result = _mean(sector_rank, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sector_rank/assets
def sibf_f082_sector_industry_biotech_filter_log_per_assets_252d_base_v073_signal(sector_rank, assets):
    s = _sector_industry_biotech_filter_scaled(sector_rank, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sector_rank/assets
def sibf_f082_sector_industry_biotech_filter_log_per_assets_504d_base_v074_signal(sector_rank, assets):
    s = _sector_industry_biotech_filter_scaled(sector_rank, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sector_rank/marketcap
def sibf_f082_sector_industry_biotech_filter_log_per_marketcap_252d_base_v075_signal(sector_rank, marketcap):
    s = _sector_industry_biotech_filter_scaled(sector_rank, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
