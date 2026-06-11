"""Family f19 - SG&A vs R&D mix  (C_RnD_Innovation) | base 001-075"""
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
def _sga_vs_rnd_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sga_vs_rnd_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sga_vs_rnd_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed sgna times closeadj
def svr_f19_sga_vs_rnd_raw_21d_base_v001_signal(sgna, closeadj):
    result = _mean(sgna, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed sgna times closeadj
def svr_f19_sga_vs_rnd_raw_63d_base_v002_signal(sgna, closeadj):
    result = _mean(sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed sgna times closeadj
def svr_f19_sga_vs_rnd_raw_126d_base_v003_signal(sgna, closeadj):
    result = _mean(sgna, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed sgna times closeadj
def svr_f19_sga_vs_rnd_raw_252d_base_v004_signal(sgna, closeadj):
    result = _mean(sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed sgna times closeadj
def svr_f19_sga_vs_rnd_raw_504d_base_v005_signal(sgna, closeadj):
    result = _mean(sgna, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(sgna) times closeadj
def svr_f19_sga_vs_rnd_log_21d_base_v006_signal(sgna, closeadj):
    result = _mean(_sga_vs_rnd_log(sgna), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(sgna) times closeadj
def svr_f19_sga_vs_rnd_log_63d_base_v007_signal(sgna, closeadj):
    result = _mean(_sga_vs_rnd_log(sgna), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(sgna) times closeadj
def svr_f19_sga_vs_rnd_log_126d_base_v008_signal(sgna, closeadj):
    result = _mean(_sga_vs_rnd_log(sgna), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(sgna) times closeadj
def svr_f19_sga_vs_rnd_log_252d_base_v009_signal(sgna, closeadj):
    result = _mean(_sga_vs_rnd_log(sgna), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(sgna) times closeadj
def svr_f19_sga_vs_rnd_log_504d_base_v010_signal(sgna, closeadj):
    result = _mean(_sga_vs_rnd_log(sgna), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/assets mean
def svr_f19_sga_vs_rnd_per_assets_63d_base_v011_signal(sgna, assets):
    result = _mean(_sga_vs_rnd_scaled(sgna, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/assets mean
def svr_f19_sga_vs_rnd_per_assets_252d_base_v012_signal(sgna, assets):
    result = _mean(_sga_vs_rnd_scaled(sgna, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/assets mean
def svr_f19_sga_vs_rnd_per_assets_504d_base_v013_signal(sgna, assets):
    result = _mean(_sga_vs_rnd_scaled(sgna, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/marketcap mean
def svr_f19_sga_vs_rnd_per_marketcap_63d_base_v014_signal(sgna, marketcap):
    result = _mean(_sga_vs_rnd_scaled(sgna, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/marketcap mean
def svr_f19_sga_vs_rnd_per_marketcap_252d_base_v015_signal(sgna, marketcap):
    result = _mean(_sga_vs_rnd_scaled(sgna, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/marketcap mean
def svr_f19_sga_vs_rnd_per_marketcap_504d_base_v016_signal(sgna, marketcap):
    result = _mean(_sga_vs_rnd_scaled(sgna, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/equity mean
def svr_f19_sga_vs_rnd_per_equity_63d_base_v017_signal(sgna, equity):
    result = _mean(_sga_vs_rnd_scaled(sgna, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/equity mean
def svr_f19_sga_vs_rnd_per_equity_252d_base_v018_signal(sgna, equity):
    result = _mean(_sga_vs_rnd_scaled(sgna, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/equity mean
def svr_f19_sga_vs_rnd_per_equity_504d_base_v019_signal(sgna, equity):
    result = _mean(_sga_vs_rnd_scaled(sgna, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/debt mean
def svr_f19_sga_vs_rnd_per_debt_63d_base_v020_signal(sgna, debt):
    result = _mean(_sga_vs_rnd_scaled(sgna, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/debt mean
def svr_f19_sga_vs_rnd_per_debt_252d_base_v021_signal(sgna, debt):
    result = _mean(_sga_vs_rnd_scaled(sgna, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/debt mean
def svr_f19_sga_vs_rnd_per_debt_504d_base_v022_signal(sgna, debt):
    result = _mean(_sga_vs_rnd_scaled(sgna, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/revenue mean
def svr_f19_sga_vs_rnd_per_revenue_63d_base_v023_signal(sgna, revenue):
    result = _mean(_sga_vs_rnd_scaled(sgna, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/revenue mean
def svr_f19_sga_vs_rnd_per_revenue_252d_base_v024_signal(sgna, revenue):
    result = _mean(_sga_vs_rnd_scaled(sgna, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/revenue mean
def svr_f19_sga_vs_rnd_per_revenue_504d_base_v025_signal(sgna, revenue):
    result = _mean(_sga_vs_rnd_scaled(sgna, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sgna per share times closeadj
def svr_f19_sga_vs_rnd_pershare_21d_base_v026_signal(sgna, sharesbas, closeadj):
    ps = _sga_vs_rnd_per_share(sgna, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna per share times closeadj
def svr_f19_sga_vs_rnd_pershare_63d_base_v027_signal(sgna, sharesbas, closeadj):
    ps = _sga_vs_rnd_per_share(sgna, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sgna per share times closeadj
def svr_f19_sga_vs_rnd_pershare_126d_base_v028_signal(sgna, sharesbas, closeadj):
    ps = _sga_vs_rnd_per_share(sgna, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna per share times closeadj
def svr_f19_sga_vs_rnd_pershare_252d_base_v029_signal(sgna, sharesbas, closeadj):
    ps = _sga_vs_rnd_per_share(sgna, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna per share times closeadj
def svr_f19_sga_vs_rnd_pershare_504d_base_v030_signal(sgna, sharesbas, closeadj):
    ps = _sga_vs_rnd_per_share(sgna, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of sgna times closeadj
def svr_f19_sga_vs_rnd_std_63d_base_v031_signal(sgna, closeadj):
    result = _std(sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of sgna times closeadj
def svr_f19_sga_vs_rnd_std_252d_base_v032_signal(sgna, closeadj):
    result = _std(sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of sgna times closeadj
def svr_f19_sga_vs_rnd_std_504d_base_v033_signal(sgna, closeadj):
    result = _std(sgna, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of sgna
def svr_f19_sga_vs_rnd_z_252d_base_v034_signal(sgna):
    result = _z(sgna, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of sgna
def svr_f19_sga_vs_rnd_z_504d_base_v035_signal(sgna):
    result = _z(sgna, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(sgna)
def svr_f19_sga_vs_rnd_logz_252d_base_v036_signal(sgna):
    result = _z(_sga_vs_rnd_log(sgna), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(sgna)
def svr_f19_sga_vs_rnd_logz_504d_base_v037_signal(sgna):
    result = _z(_sga_vs_rnd_log(sgna), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sgna^2 times closeadj
def svr_f19_sga_vs_rnd_sq_63d_base_v038_signal(sgna, closeadj):
    result = _mean(sgna * sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sgna^2 times closeadj
def svr_f19_sga_vs_rnd_sq_252d_base_v039_signal(sgna, closeadj):
    result = _mean(sgna * sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(sgna) times closeadj
def svr_f19_sga_vs_rnd_sign_21d_base_v040_signal(sgna, closeadj):
    result = _mean(np.sign(sgna), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(sgna) times closeadj
def svr_f19_sga_vs_rnd_sign_63d_base_v041_signal(sgna, closeadj):
    result = _mean(np.sign(sgna), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(sgna) times closeadj
def svr_f19_sga_vs_rnd_sign_252d_base_v042_signal(sgna, closeadj):
    result = _mean(np.sign(sgna), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/opex mean
def svr_f19_sga_vs_rnd_per_opex_63d_base_v043_signal(sgna, opex):
    result = _mean(_sga_vs_rnd_scaled(sgna, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/opex mean
def svr_f19_sga_vs_rnd_per_opex_252d_base_v044_signal(sgna, opex):
    result = _mean(_sga_vs_rnd_scaled(sgna, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/ebitda mean
def svr_f19_sga_vs_rnd_per_ebitda_63d_base_v045_signal(sgna, ebitda):
    result = _mean(_sga_vs_rnd_scaled(sgna, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/ebitda mean
def svr_f19_sga_vs_rnd_per_ebitda_252d_base_v046_signal(sgna, ebitda):
    result = _mean(_sga_vs_rnd_scaled(sgna, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/capex mean
def svr_f19_sga_vs_rnd_per_capex_63d_base_v047_signal(sgna, capex):
    result = _mean(_sga_vs_rnd_scaled(sgna, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/capex mean
def svr_f19_sga_vs_rnd_per_capex_252d_base_v048_signal(sgna, capex):
    result = _mean(_sga_vs_rnd_scaled(sgna, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/liabilities mean
def svr_f19_sga_vs_rnd_per_liabilities_63d_base_v049_signal(sgna, liabilities):
    result = _mean(_sga_vs_rnd_scaled(sgna, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/liabilities mean
def svr_f19_sga_vs_rnd_per_liabilities_252d_base_v050_signal(sgna, liabilities):
    result = _mean(_sga_vs_rnd_scaled(sgna, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 252d max times closeadj
def svr_f19_sga_vs_rnd_relmax_252d_base_v051_signal(sgna, closeadj):
    peak = sgna.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (sgna / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 504d max times closeadj
def svr_f19_sga_vs_rnd_relmax_504d_base_v052_signal(sgna, closeadj):
    peak = sgna.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (sgna / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 252d min times closeadj
def svr_f19_sga_vs_rnd_relmin_252d_base_v053_signal(sgna, closeadj):
    trough = sgna.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (sgna / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 504d min times closeadj
def svr_f19_sga_vs_rnd_relmin_504d_base_v054_signal(sgna, closeadj):
    trough = sgna.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (sgna / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of sgna times closeadj
def svr_f19_sga_vs_rnd_pct_21d_base_v055_signal(sgna, closeadj):
    result = _pct_change(sgna, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of sgna times closeadj
def svr_f19_sga_vs_rnd_pct_63d_base_v056_signal(sgna, closeadj):
    result = _pct_change(sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of sgna times closeadj
def svr_f19_sga_vs_rnd_pct_252d_base_v057_signal(sgna, closeadj):
    result = _pct_change(sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of sgna times closeadj
def svr_f19_sga_vs_rnd_sum_63d_base_v058_signal(sgna, closeadj):
    result = sgna.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of sgna times closeadj
def svr_f19_sga_vs_rnd_sum_252d_base_v059_signal(sgna, closeadj):
    result = sgna.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of sgna times closeadj
def svr_f19_sga_vs_rnd_sum_504d_base_v060_signal(sgna, closeadj):
    result = sgna.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(63d) / smoothed assets(252d) x closeadj
def svr_f19_sga_vs_rnd_rom_assets_252_63d_base_v061_signal(sgna, assets, closeadj):
    n = _mean(sgna, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(126d) / smoothed assets(504d) x closeadj
def svr_f19_sga_vs_rnd_rom_assets_504_126d_base_v062_signal(sgna, assets, closeadj):
    n = _mean(sgna, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(63d) / smoothed marketcap(252d) x closeadj
def svr_f19_sga_vs_rnd_rom_marketcap_252_63d_base_v063_signal(sgna, marketcap, closeadj):
    n = _mean(sgna, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(126d) / smoothed marketcap(504d) x closeadj
def svr_f19_sga_vs_rnd_rom_marketcap_504_126d_base_v064_signal(sgna, marketcap, closeadj):
    n = _mean(sgna, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(63d) / smoothed equity(252d) x closeadj
def svr_f19_sga_vs_rnd_rom_equity_252_63d_base_v065_signal(sgna, equity, closeadj):
    n = _mean(sgna, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(126d) / smoothed equity(504d) x closeadj
def svr_f19_sga_vs_rnd_rom_equity_504_126d_base_v066_signal(sgna, equity, closeadj):
    n = _mean(sgna, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sgna) / std(assets)
def svr_f19_sga_vs_rnd_volratio_assets_252d_base_v067_signal(sgna, assets):
    n = _std(sgna, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sgna) / std(assets)
def svr_f19_sga_vs_rnd_volratio_assets_504d_base_v068_signal(sgna, assets):
    n = _std(sgna, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sgna) / std(marketcap)
def svr_f19_sga_vs_rnd_volratio_marketcap_252d_base_v069_signal(sgna, marketcap):
    n = _std(sgna, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sgna) / std(marketcap)
def svr_f19_sga_vs_rnd_volratio_marketcap_504d_base_v070_signal(sgna, marketcap):
    n = _std(sgna, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed sgna times closeadj
def svr_f19_sga_vs_rnd_raw_5d_base_v071_signal(sgna, closeadj):
    result = _mean(sgna, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed sgna times closeadj
def svr_f19_sga_vs_rnd_raw_1008d_base_v072_signal(sgna, closeadj):
    result = _mean(sgna, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sgna/assets
def svr_f19_sga_vs_rnd_log_per_assets_252d_base_v073_signal(sgna, assets):
    s = _sga_vs_rnd_scaled(sgna, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sgna/assets
def svr_f19_sga_vs_rnd_log_per_assets_504d_base_v074_signal(sgna, assets):
    s = _sga_vs_rnd_scaled(sgna, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sgna/marketcap
def svr_f19_sga_vs_rnd_log_per_marketcap_252d_base_v075_signal(sgna, marketcap):
    s = _sga_vs_rnd_scaled(sgna, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
