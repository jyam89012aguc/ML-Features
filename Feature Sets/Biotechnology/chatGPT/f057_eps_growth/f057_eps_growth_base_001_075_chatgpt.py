"""Family f057 - EPS growth and improvement (Earnings and Quality) | Sharadar tables: SF1 | fields: eps, epsdil | base 001-075"""
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
def _eps_growth_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _eps_growth_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _eps_growth_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed eps times closeadj
def eg_f057_eps_growth_raw_21d_base_v001_signal(eps, closeadj):
    result = _mean(eps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed eps times closeadj
def eg_f057_eps_growth_raw_63d_base_v002_signal(eps, closeadj):
    result = _mean(eps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed eps times closeadj
def eg_f057_eps_growth_raw_126d_base_v003_signal(eps, closeadj):
    result = _mean(eps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed eps times closeadj
def eg_f057_eps_growth_raw_252d_base_v004_signal(eps, closeadj):
    result = _mean(eps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed eps times closeadj
def eg_f057_eps_growth_raw_504d_base_v005_signal(eps, closeadj):
    result = _mean(eps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(eps) times closeadj
def eg_f057_eps_growth_log_21d_base_v006_signal(eps, closeadj):
    result = _mean(_eps_growth_log(eps), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(eps) times closeadj
def eg_f057_eps_growth_log_63d_base_v007_signal(eps, closeadj):
    result = _mean(_eps_growth_log(eps), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(eps) times closeadj
def eg_f057_eps_growth_log_126d_base_v008_signal(eps, closeadj):
    result = _mean(_eps_growth_log(eps), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(eps) times closeadj
def eg_f057_eps_growth_log_252d_base_v009_signal(eps, closeadj):
    result = _mean(_eps_growth_log(eps), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(eps) times closeadj
def eg_f057_eps_growth_log_504d_base_v010_signal(eps, closeadj):
    result = _mean(_eps_growth_log(eps), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps/epsdil mean
def eg_f057_eps_growth_per_epsdil_63d_base_v011_signal(eps, epsdil):
    result = _mean(_eps_growth_scaled(eps, epsdil), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps/epsdil mean
def eg_f057_eps_growth_per_epsdil_252d_base_v012_signal(eps, epsdil):
    result = _mean(_eps_growth_scaled(eps, epsdil), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d eps/epsdil mean
def eg_f057_eps_growth_per_epsdil_504d_base_v013_signal(eps, epsdil):
    result = _mean(_eps_growth_scaled(eps, epsdil), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps/assets mean
def eg_f057_eps_growth_per_assets_63d_base_v014_signal(eps, assets):
    result = _mean(_eps_growth_scaled(eps, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps/assets mean
def eg_f057_eps_growth_per_assets_252d_base_v015_signal(eps, assets):
    result = _mean(_eps_growth_scaled(eps, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d eps/assets mean
def eg_f057_eps_growth_per_assets_504d_base_v016_signal(eps, assets):
    result = _mean(_eps_growth_scaled(eps, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps/marketcap mean
def eg_f057_eps_growth_per_marketcap_63d_base_v017_signal(eps, marketcap):
    result = _mean(_eps_growth_scaled(eps, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps/marketcap mean
def eg_f057_eps_growth_per_marketcap_252d_base_v018_signal(eps, marketcap):
    result = _mean(_eps_growth_scaled(eps, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d eps/marketcap mean
def eg_f057_eps_growth_per_marketcap_504d_base_v019_signal(eps, marketcap):
    result = _mean(_eps_growth_scaled(eps, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps/equity mean
def eg_f057_eps_growth_per_equity_63d_base_v020_signal(eps, equity):
    result = _mean(_eps_growth_scaled(eps, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps/equity mean
def eg_f057_eps_growth_per_equity_252d_base_v021_signal(eps, equity):
    result = _mean(_eps_growth_scaled(eps, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d eps/equity mean
def eg_f057_eps_growth_per_equity_504d_base_v022_signal(eps, equity):
    result = _mean(_eps_growth_scaled(eps, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps/debt mean
def eg_f057_eps_growth_per_debt_63d_base_v023_signal(eps, debt):
    result = _mean(_eps_growth_scaled(eps, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps/debt mean
def eg_f057_eps_growth_per_debt_252d_base_v024_signal(eps, debt):
    result = _mean(_eps_growth_scaled(eps, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d eps/debt mean
def eg_f057_eps_growth_per_debt_504d_base_v025_signal(eps, debt):
    result = _mean(_eps_growth_scaled(eps, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d eps per share times closeadj
def eg_f057_eps_growth_pershare_21d_base_v026_signal(eps, sharesbas, closeadj):
    ps = _eps_growth_per_share(eps, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps per share times closeadj
def eg_f057_eps_growth_pershare_63d_base_v027_signal(eps, sharesbas, closeadj):
    ps = _eps_growth_per_share(eps, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d eps per share times closeadj
def eg_f057_eps_growth_pershare_126d_base_v028_signal(eps, sharesbas, closeadj):
    ps = _eps_growth_per_share(eps, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps per share times closeadj
def eg_f057_eps_growth_pershare_252d_base_v029_signal(eps, sharesbas, closeadj):
    ps = _eps_growth_per_share(eps, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d eps per share times closeadj
def eg_f057_eps_growth_pershare_504d_base_v030_signal(eps, sharesbas, closeadj):
    ps = _eps_growth_per_share(eps, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of eps times closeadj
def eg_f057_eps_growth_std_63d_base_v031_signal(eps, closeadj):
    result = _std(eps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of eps times closeadj
def eg_f057_eps_growth_std_252d_base_v032_signal(eps, closeadj):
    result = _std(eps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of eps times closeadj
def eg_f057_eps_growth_std_504d_base_v033_signal(eps, closeadj):
    result = _std(eps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of eps
def eg_f057_eps_growth_z_252d_base_v034_signal(eps):
    result = _z(eps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of eps
def eg_f057_eps_growth_z_504d_base_v035_signal(eps):
    result = _z(eps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(eps)
def eg_f057_eps_growth_logz_252d_base_v036_signal(eps):
    result = _z(_eps_growth_log(eps), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(eps)
def eg_f057_eps_growth_logz_504d_base_v037_signal(eps):
    result = _z(_eps_growth_log(eps), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of eps^2 times closeadj
def eg_f057_eps_growth_sq_63d_base_v038_signal(eps, closeadj):
    result = _mean(eps * eps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of eps^2 times closeadj
def eg_f057_eps_growth_sq_252d_base_v039_signal(eps, closeadj):
    result = _mean(eps * eps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(eps) times closeadj
def eg_f057_eps_growth_sign_21d_base_v040_signal(eps, closeadj):
    result = _mean(np.sign(eps), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(eps) times closeadj
def eg_f057_eps_growth_sign_63d_base_v041_signal(eps, closeadj):
    result = _mean(np.sign(eps), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(eps) times closeadj
def eg_f057_eps_growth_sign_252d_base_v042_signal(eps, closeadj):
    result = _mean(np.sign(eps), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps/opex mean
def eg_f057_eps_growth_per_opex_63d_base_v043_signal(eps, opex):
    result = _mean(_eps_growth_scaled(eps, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps/opex mean
def eg_f057_eps_growth_per_opex_252d_base_v044_signal(eps, opex):
    result = _mean(_eps_growth_scaled(eps, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps/ebitda mean
def eg_f057_eps_growth_per_ebitda_63d_base_v045_signal(eps, ebitda):
    result = _mean(_eps_growth_scaled(eps, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps/ebitda mean
def eg_f057_eps_growth_per_ebitda_252d_base_v046_signal(eps, ebitda):
    result = _mean(_eps_growth_scaled(eps, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps/capex mean
def eg_f057_eps_growth_per_capex_63d_base_v047_signal(eps, capex):
    result = _mean(_eps_growth_scaled(eps, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps/capex mean
def eg_f057_eps_growth_per_capex_252d_base_v048_signal(eps, capex):
    result = _mean(_eps_growth_scaled(eps, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eps/liabilities mean
def eg_f057_eps_growth_per_liabilities_63d_base_v049_signal(eps, liabilities):
    result = _mean(_eps_growth_scaled(eps, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps/liabilities mean
def eg_f057_eps_growth_per_liabilities_252d_base_v050_signal(eps, liabilities):
    result = _mean(_eps_growth_scaled(eps, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# eps relative to 252d max times closeadj
def eg_f057_eps_growth_relmax_252d_base_v051_signal(eps, closeadj):
    peak = eps.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (eps / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eps relative to 504d max times closeadj
def eg_f057_eps_growth_relmax_504d_base_v052_signal(eps, closeadj):
    peak = eps.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (eps / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eps relative to 252d min times closeadj
def eg_f057_eps_growth_relmin_252d_base_v053_signal(eps, closeadj):
    trough = eps.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (eps / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eps relative to 504d min times closeadj
def eg_f057_eps_growth_relmin_504d_base_v054_signal(eps, closeadj):
    trough = eps.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (eps / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of eps times closeadj
def eg_f057_eps_growth_pct_21d_base_v055_signal(eps, closeadj):
    result = _pct_change(eps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of eps times closeadj
def eg_f057_eps_growth_pct_63d_base_v056_signal(eps, closeadj):
    result = _pct_change(eps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of eps times closeadj
def eg_f057_eps_growth_pct_252d_base_v057_signal(eps, closeadj):
    result = _pct_change(eps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of eps times closeadj
def eg_f057_eps_growth_sum_63d_base_v058_signal(eps, closeadj):
    result = eps.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of eps times closeadj
def eg_f057_eps_growth_sum_252d_base_v059_signal(eps, closeadj):
    result = eps.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of eps times closeadj
def eg_f057_eps_growth_sum_504d_base_v060_signal(eps, closeadj):
    result = eps.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed eps(63d) / smoothed epsdil(252d) x closeadj
def eg_f057_eps_growth_rom_epsdil_252_63d_base_v061_signal(eps, epsdil, closeadj):
    n = _mean(eps, 63)
    d = _mean(epsdil, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed eps(126d) / smoothed epsdil(504d) x closeadj
def eg_f057_eps_growth_rom_epsdil_504_126d_base_v062_signal(eps, epsdil, closeadj):
    n = _mean(eps, 126)
    d = _mean(epsdil, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed eps(63d) / smoothed assets(252d) x closeadj
def eg_f057_eps_growth_rom_assets_252_63d_base_v063_signal(eps, assets, closeadj):
    n = _mean(eps, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed eps(126d) / smoothed assets(504d) x closeadj
def eg_f057_eps_growth_rom_assets_504_126d_base_v064_signal(eps, assets, closeadj):
    n = _mean(eps, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed eps(63d) / smoothed marketcap(252d) x closeadj
def eg_f057_eps_growth_rom_marketcap_252_63d_base_v065_signal(eps, marketcap, closeadj):
    n = _mean(eps, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed eps(126d) / smoothed marketcap(504d) x closeadj
def eg_f057_eps_growth_rom_marketcap_504_126d_base_v066_signal(eps, marketcap, closeadj):
    n = _mean(eps, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(eps) / std(epsdil)
def eg_f057_eps_growth_volratio_epsdil_252d_base_v067_signal(eps, epsdil):
    n = _std(eps, 252)
    d = _std(epsdil, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(eps) / std(epsdil)
def eg_f057_eps_growth_volratio_epsdil_504d_base_v068_signal(eps, epsdil):
    n = _std(eps, 504)
    d = _std(epsdil, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(eps) / std(assets)
def eg_f057_eps_growth_volratio_assets_252d_base_v069_signal(eps, assets):
    n = _std(eps, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(eps) / std(assets)
def eg_f057_eps_growth_volratio_assets_504d_base_v070_signal(eps, assets):
    n = _std(eps, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed eps times closeadj
def eg_f057_eps_growth_raw_5d_base_v071_signal(eps, closeadj):
    result = _mean(eps, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed eps times closeadj
def eg_f057_eps_growth_raw_1008d_base_v072_signal(eps, closeadj):
    result = _mean(eps, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of eps/epsdil
def eg_f057_eps_growth_log_per_epsdil_252d_base_v073_signal(eps, epsdil):
    s = _eps_growth_scaled(eps, epsdil)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of eps/epsdil
def eg_f057_eps_growth_log_per_epsdil_504d_base_v074_signal(eps, epsdil):
    s = _eps_growth_scaled(eps, epsdil)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of eps/assets
def eg_f057_eps_growth_log_per_assets_252d_base_v075_signal(eps, assets):
    s = _eps_growth_scaled(eps, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
