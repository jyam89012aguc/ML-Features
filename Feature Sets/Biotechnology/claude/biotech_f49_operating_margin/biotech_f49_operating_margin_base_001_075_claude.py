"""Family f49 - Operating margin  (H_Margins) | base 001-075"""
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
def _operating_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _operating_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _operating_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed opinc times closeadj
def om_f49_operating_margin_raw_21d_base_v001_signal(opinc, closeadj):
    result = _mean(opinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed opinc times closeadj
def om_f49_operating_margin_raw_63d_base_v002_signal(opinc, closeadj):
    result = _mean(opinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed opinc times closeadj
def om_f49_operating_margin_raw_126d_base_v003_signal(opinc, closeadj):
    result = _mean(opinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed opinc times closeadj
def om_f49_operating_margin_raw_252d_base_v004_signal(opinc, closeadj):
    result = _mean(opinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed opinc times closeadj
def om_f49_operating_margin_raw_504d_base_v005_signal(opinc, closeadj):
    result = _mean(opinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(opinc) times closeadj
def om_f49_operating_margin_log_21d_base_v006_signal(opinc, closeadj):
    result = _mean(_operating_margin_log(opinc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(opinc) times closeadj
def om_f49_operating_margin_log_63d_base_v007_signal(opinc, closeadj):
    result = _mean(_operating_margin_log(opinc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(opinc) times closeadj
def om_f49_operating_margin_log_126d_base_v008_signal(opinc, closeadj):
    result = _mean(_operating_margin_log(opinc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(opinc) times closeadj
def om_f49_operating_margin_log_252d_base_v009_signal(opinc, closeadj):
    result = _mean(_operating_margin_log(opinc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(opinc) times closeadj
def om_f49_operating_margin_log_504d_base_v010_signal(opinc, closeadj):
    result = _mean(_operating_margin_log(opinc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/assets mean
def om_f49_operating_margin_per_assets_63d_base_v011_signal(opinc, assets):
    result = _mean(_operating_margin_scaled(opinc, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/assets mean
def om_f49_operating_margin_per_assets_252d_base_v012_signal(opinc, assets):
    result = _mean(_operating_margin_scaled(opinc, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opinc/assets mean
def om_f49_operating_margin_per_assets_504d_base_v013_signal(opinc, assets):
    result = _mean(_operating_margin_scaled(opinc, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/marketcap mean
def om_f49_operating_margin_per_marketcap_63d_base_v014_signal(opinc, marketcap):
    result = _mean(_operating_margin_scaled(opinc, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/marketcap mean
def om_f49_operating_margin_per_marketcap_252d_base_v015_signal(opinc, marketcap):
    result = _mean(_operating_margin_scaled(opinc, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opinc/marketcap mean
def om_f49_operating_margin_per_marketcap_504d_base_v016_signal(opinc, marketcap):
    result = _mean(_operating_margin_scaled(opinc, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/equity mean
def om_f49_operating_margin_per_equity_63d_base_v017_signal(opinc, equity):
    result = _mean(_operating_margin_scaled(opinc, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/equity mean
def om_f49_operating_margin_per_equity_252d_base_v018_signal(opinc, equity):
    result = _mean(_operating_margin_scaled(opinc, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opinc/equity mean
def om_f49_operating_margin_per_equity_504d_base_v019_signal(opinc, equity):
    result = _mean(_operating_margin_scaled(opinc, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/debt mean
def om_f49_operating_margin_per_debt_63d_base_v020_signal(opinc, debt):
    result = _mean(_operating_margin_scaled(opinc, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/debt mean
def om_f49_operating_margin_per_debt_252d_base_v021_signal(opinc, debt):
    result = _mean(_operating_margin_scaled(opinc, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opinc/debt mean
def om_f49_operating_margin_per_debt_504d_base_v022_signal(opinc, debt):
    result = _mean(_operating_margin_scaled(opinc, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/revenue mean
def om_f49_operating_margin_per_revenue_63d_base_v023_signal(opinc, revenue):
    result = _mean(_operating_margin_scaled(opinc, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/revenue mean
def om_f49_operating_margin_per_revenue_252d_base_v024_signal(opinc, revenue):
    result = _mean(_operating_margin_scaled(opinc, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opinc/revenue mean
def om_f49_operating_margin_per_revenue_504d_base_v025_signal(opinc, revenue):
    result = _mean(_operating_margin_scaled(opinc, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d opinc per share times closeadj
def om_f49_operating_margin_pershare_21d_base_v026_signal(opinc, sharesbas, closeadj):
    ps = _operating_margin_per_share(opinc, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc per share times closeadj
def om_f49_operating_margin_pershare_63d_base_v027_signal(opinc, sharesbas, closeadj):
    ps = _operating_margin_per_share(opinc, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d opinc per share times closeadj
def om_f49_operating_margin_pershare_126d_base_v028_signal(opinc, sharesbas, closeadj):
    ps = _operating_margin_per_share(opinc, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc per share times closeadj
def om_f49_operating_margin_pershare_252d_base_v029_signal(opinc, sharesbas, closeadj):
    ps = _operating_margin_per_share(opinc, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opinc per share times closeadj
def om_f49_operating_margin_pershare_504d_base_v030_signal(opinc, sharesbas, closeadj):
    ps = _operating_margin_per_share(opinc, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of opinc times closeadj
def om_f49_operating_margin_std_63d_base_v031_signal(opinc, closeadj):
    result = _std(opinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of opinc times closeadj
def om_f49_operating_margin_std_252d_base_v032_signal(opinc, closeadj):
    result = _std(opinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of opinc times closeadj
def om_f49_operating_margin_std_504d_base_v033_signal(opinc, closeadj):
    result = _std(opinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of opinc
def om_f49_operating_margin_z_252d_base_v034_signal(opinc):
    result = _z(opinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of opinc
def om_f49_operating_margin_z_504d_base_v035_signal(opinc):
    result = _z(opinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(opinc)
def om_f49_operating_margin_logz_252d_base_v036_signal(opinc):
    result = _z(_operating_margin_log(opinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(opinc)
def om_f49_operating_margin_logz_504d_base_v037_signal(opinc):
    result = _z(_operating_margin_log(opinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of opinc^2 times closeadj
def om_f49_operating_margin_sq_63d_base_v038_signal(opinc, closeadj):
    result = _mean(opinc * opinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of opinc^2 times closeadj
def om_f49_operating_margin_sq_252d_base_v039_signal(opinc, closeadj):
    result = _mean(opinc * opinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(opinc) times closeadj
def om_f49_operating_margin_sign_21d_base_v040_signal(opinc, closeadj):
    result = _mean(np.sign(opinc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(opinc) times closeadj
def om_f49_operating_margin_sign_63d_base_v041_signal(opinc, closeadj):
    result = _mean(np.sign(opinc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(opinc) times closeadj
def om_f49_operating_margin_sign_252d_base_v042_signal(opinc, closeadj):
    result = _mean(np.sign(opinc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/opex mean
def om_f49_operating_margin_per_opex_63d_base_v043_signal(opinc, opex):
    result = _mean(_operating_margin_scaled(opinc, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/opex mean
def om_f49_operating_margin_per_opex_252d_base_v044_signal(opinc, opex):
    result = _mean(_operating_margin_scaled(opinc, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/ebitda mean
def om_f49_operating_margin_per_ebitda_63d_base_v045_signal(opinc, ebitda):
    result = _mean(_operating_margin_scaled(opinc, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/ebitda mean
def om_f49_operating_margin_per_ebitda_252d_base_v046_signal(opinc, ebitda):
    result = _mean(_operating_margin_scaled(opinc, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/capex mean
def om_f49_operating_margin_per_capex_63d_base_v047_signal(opinc, capex):
    result = _mean(_operating_margin_scaled(opinc, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/capex mean
def om_f49_operating_margin_per_capex_252d_base_v048_signal(opinc, capex):
    result = _mean(_operating_margin_scaled(opinc, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/liabilities mean
def om_f49_operating_margin_per_liabilities_63d_base_v049_signal(opinc, liabilities):
    result = _mean(_operating_margin_scaled(opinc, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/liabilities mean
def om_f49_operating_margin_per_liabilities_252d_base_v050_signal(opinc, liabilities):
    result = _mean(_operating_margin_scaled(opinc, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# opinc relative to 252d max times closeadj
def om_f49_operating_margin_relmax_252d_base_v051_signal(opinc, closeadj):
    peak = opinc.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (opinc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opinc relative to 504d max times closeadj
def om_f49_operating_margin_relmax_504d_base_v052_signal(opinc, closeadj):
    peak = opinc.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (opinc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opinc relative to 252d min times closeadj
def om_f49_operating_margin_relmin_252d_base_v053_signal(opinc, closeadj):
    trough = opinc.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (opinc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opinc relative to 504d min times closeadj
def om_f49_operating_margin_relmin_504d_base_v054_signal(opinc, closeadj):
    trough = opinc.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (opinc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of opinc times closeadj
def om_f49_operating_margin_pct_21d_base_v055_signal(opinc, closeadj):
    result = _pct_change(opinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of opinc times closeadj
def om_f49_operating_margin_pct_63d_base_v056_signal(opinc, closeadj):
    result = _pct_change(opinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of opinc times closeadj
def om_f49_operating_margin_pct_252d_base_v057_signal(opinc, closeadj):
    result = _pct_change(opinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of opinc times closeadj
def om_f49_operating_margin_sum_63d_base_v058_signal(opinc, closeadj):
    result = opinc.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of opinc times closeadj
def om_f49_operating_margin_sum_252d_base_v059_signal(opinc, closeadj):
    result = opinc.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of opinc times closeadj
def om_f49_operating_margin_sum_504d_base_v060_signal(opinc, closeadj):
    result = opinc.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed opinc(63d) / smoothed assets(252d) x closeadj
def om_f49_operating_margin_rom_assets_252_63d_base_v061_signal(opinc, assets, closeadj):
    n = _mean(opinc, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed opinc(126d) / smoothed assets(504d) x closeadj
def om_f49_operating_margin_rom_assets_504_126d_base_v062_signal(opinc, assets, closeadj):
    n = _mean(opinc, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed opinc(63d) / smoothed marketcap(252d) x closeadj
def om_f49_operating_margin_rom_marketcap_252_63d_base_v063_signal(opinc, marketcap, closeadj):
    n = _mean(opinc, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed opinc(126d) / smoothed marketcap(504d) x closeadj
def om_f49_operating_margin_rom_marketcap_504_126d_base_v064_signal(opinc, marketcap, closeadj):
    n = _mean(opinc, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed opinc(63d) / smoothed equity(252d) x closeadj
def om_f49_operating_margin_rom_equity_252_63d_base_v065_signal(opinc, equity, closeadj):
    n = _mean(opinc, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed opinc(126d) / smoothed equity(504d) x closeadj
def om_f49_operating_margin_rom_equity_504_126d_base_v066_signal(opinc, equity, closeadj):
    n = _mean(opinc, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(opinc) / std(assets)
def om_f49_operating_margin_volratio_assets_252d_base_v067_signal(opinc, assets):
    n = _std(opinc, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(opinc) / std(assets)
def om_f49_operating_margin_volratio_assets_504d_base_v068_signal(opinc, assets):
    n = _std(opinc, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(opinc) / std(marketcap)
def om_f49_operating_margin_volratio_marketcap_252d_base_v069_signal(opinc, marketcap):
    n = _std(opinc, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(opinc) / std(marketcap)
def om_f49_operating_margin_volratio_marketcap_504d_base_v070_signal(opinc, marketcap):
    n = _std(opinc, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed opinc times closeadj
def om_f49_operating_margin_raw_5d_base_v071_signal(opinc, closeadj):
    result = _mean(opinc, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed opinc times closeadj
def om_f49_operating_margin_raw_1008d_base_v072_signal(opinc, closeadj):
    result = _mean(opinc, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of opinc/assets
def om_f49_operating_margin_log_per_assets_252d_base_v073_signal(opinc, assets):
    s = _operating_margin_scaled(opinc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of opinc/assets
def om_f49_operating_margin_log_per_assets_504d_base_v074_signal(opinc, assets):
    s = _operating_margin_scaled(opinc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of opinc/marketcap
def om_f49_operating_margin_log_per_marketcap_252d_base_v075_signal(opinc, marketcap):
    s = _operating_margin_scaled(opinc, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
