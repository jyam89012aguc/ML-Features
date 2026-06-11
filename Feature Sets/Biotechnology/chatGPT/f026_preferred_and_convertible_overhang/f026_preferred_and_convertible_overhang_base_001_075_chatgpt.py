"""Family f026 - preferred, convertible, and senior claim overhang (Capital Structure) | Sharadar tables: SF1 | fields: prefdivis, debtusd, assets, marketcap, equity, debt | base 001-075"""
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
def _preferred_and_convertible_overhang_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _preferred_and_convertible_overhang_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _preferred_and_convertible_overhang_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_raw_21d_base_v001_signal(prefdivis, closeadj):
    result = _mean(prefdivis, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_raw_63d_base_v002_signal(prefdivis, closeadj):
    result = _mean(prefdivis, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_raw_126d_base_v003_signal(prefdivis, closeadj):
    result = _mean(prefdivis, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_raw_252d_base_v004_signal(prefdivis, closeadj):
    result = _mean(prefdivis, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_raw_504d_base_v005_signal(prefdivis, closeadj):
    result = _mean(prefdivis, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(prefdivis) times closeadj
def paco_f026_preferred_and_convertible_overhang_log_21d_base_v006_signal(prefdivis, closeadj):
    result = _mean(_preferred_and_convertible_overhang_log(prefdivis), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(prefdivis) times closeadj
def paco_f026_preferred_and_convertible_overhang_log_63d_base_v007_signal(prefdivis, closeadj):
    result = _mean(_preferred_and_convertible_overhang_log(prefdivis), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(prefdivis) times closeadj
def paco_f026_preferred_and_convertible_overhang_log_126d_base_v008_signal(prefdivis, closeadj):
    result = _mean(_preferred_and_convertible_overhang_log(prefdivis), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(prefdivis) times closeadj
def paco_f026_preferred_and_convertible_overhang_log_252d_base_v009_signal(prefdivis, closeadj):
    result = _mean(_preferred_and_convertible_overhang_log(prefdivis), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(prefdivis) times closeadj
def paco_f026_preferred_and_convertible_overhang_log_504d_base_v010_signal(prefdivis, closeadj):
    result = _mean(_preferred_and_convertible_overhang_log(prefdivis), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis/debtusd mean
def paco_f026_preferred_and_convertible_overhang_per_debtusd_63d_base_v011_signal(prefdivis, debtusd):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis/debtusd mean
def paco_f026_preferred_and_convertible_overhang_per_debtusd_252d_base_v012_signal(prefdivis, debtusd):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d prefdivis/debtusd mean
def paco_f026_preferred_and_convertible_overhang_per_debtusd_504d_base_v013_signal(prefdivis, debtusd):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis/assets mean
def paco_f026_preferred_and_convertible_overhang_per_assets_63d_base_v014_signal(prefdivis, assets):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis/assets mean
def paco_f026_preferred_and_convertible_overhang_per_assets_252d_base_v015_signal(prefdivis, assets):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d prefdivis/assets mean
def paco_f026_preferred_and_convertible_overhang_per_assets_504d_base_v016_signal(prefdivis, assets):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis/marketcap mean
def paco_f026_preferred_and_convertible_overhang_per_marketcap_63d_base_v017_signal(prefdivis, marketcap):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis/marketcap mean
def paco_f026_preferred_and_convertible_overhang_per_marketcap_252d_base_v018_signal(prefdivis, marketcap):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d prefdivis/marketcap mean
def paco_f026_preferred_and_convertible_overhang_per_marketcap_504d_base_v019_signal(prefdivis, marketcap):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis/equity mean
def paco_f026_preferred_and_convertible_overhang_per_equity_63d_base_v020_signal(prefdivis, equity):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis/equity mean
def paco_f026_preferred_and_convertible_overhang_per_equity_252d_base_v021_signal(prefdivis, equity):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d prefdivis/equity mean
def paco_f026_preferred_and_convertible_overhang_per_equity_504d_base_v022_signal(prefdivis, equity):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis/debt mean
def paco_f026_preferred_and_convertible_overhang_per_debt_63d_base_v023_signal(prefdivis, debt):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis/debt mean
def paco_f026_preferred_and_convertible_overhang_per_debt_252d_base_v024_signal(prefdivis, debt):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d prefdivis/debt mean
def paco_f026_preferred_and_convertible_overhang_per_debt_504d_base_v025_signal(prefdivis, debt):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d prefdivis per share times closeadj
def paco_f026_preferred_and_convertible_overhang_pershare_21d_base_v026_signal(prefdivis, sharesbas, closeadj):
    ps = _preferred_and_convertible_overhang_per_share(prefdivis, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis per share times closeadj
def paco_f026_preferred_and_convertible_overhang_pershare_63d_base_v027_signal(prefdivis, sharesbas, closeadj):
    ps = _preferred_and_convertible_overhang_per_share(prefdivis, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d prefdivis per share times closeadj
def paco_f026_preferred_and_convertible_overhang_pershare_126d_base_v028_signal(prefdivis, sharesbas, closeadj):
    ps = _preferred_and_convertible_overhang_per_share(prefdivis, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis per share times closeadj
def paco_f026_preferred_and_convertible_overhang_pershare_252d_base_v029_signal(prefdivis, sharesbas, closeadj):
    ps = _preferred_and_convertible_overhang_per_share(prefdivis, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d prefdivis per share times closeadj
def paco_f026_preferred_and_convertible_overhang_pershare_504d_base_v030_signal(prefdivis, sharesbas, closeadj):
    ps = _preferred_and_convertible_overhang_per_share(prefdivis, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_std_63d_base_v031_signal(prefdivis, closeadj):
    result = _std(prefdivis, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_std_252d_base_v032_signal(prefdivis, closeadj):
    result = _std(prefdivis, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_std_504d_base_v033_signal(prefdivis, closeadj):
    result = _std(prefdivis, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of prefdivis
def paco_f026_preferred_and_convertible_overhang_z_252d_base_v034_signal(prefdivis):
    result = _z(prefdivis, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of prefdivis
def paco_f026_preferred_and_convertible_overhang_z_504d_base_v035_signal(prefdivis):
    result = _z(prefdivis, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(prefdivis)
def paco_f026_preferred_and_convertible_overhang_logz_252d_base_v036_signal(prefdivis):
    result = _z(_preferred_and_convertible_overhang_log(prefdivis), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(prefdivis)
def paco_f026_preferred_and_convertible_overhang_logz_504d_base_v037_signal(prefdivis):
    result = _z(_preferred_and_convertible_overhang_log(prefdivis), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of prefdivis^2 times closeadj
def paco_f026_preferred_and_convertible_overhang_sq_63d_base_v038_signal(prefdivis, closeadj):
    result = _mean(prefdivis * prefdivis, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of prefdivis^2 times closeadj
def paco_f026_preferred_and_convertible_overhang_sq_252d_base_v039_signal(prefdivis, closeadj):
    result = _mean(prefdivis * prefdivis, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(prefdivis) times closeadj
def paco_f026_preferred_and_convertible_overhang_sign_21d_base_v040_signal(prefdivis, closeadj):
    result = _mean(np.sign(prefdivis), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(prefdivis) times closeadj
def paco_f026_preferred_and_convertible_overhang_sign_63d_base_v041_signal(prefdivis, closeadj):
    result = _mean(np.sign(prefdivis), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(prefdivis) times closeadj
def paco_f026_preferred_and_convertible_overhang_sign_252d_base_v042_signal(prefdivis, closeadj):
    result = _mean(np.sign(prefdivis), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis/opex mean
def paco_f026_preferred_and_convertible_overhang_per_opex_63d_base_v043_signal(prefdivis, opex):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis/opex mean
def paco_f026_preferred_and_convertible_overhang_per_opex_252d_base_v044_signal(prefdivis, opex):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis/ebitda mean
def paco_f026_preferred_and_convertible_overhang_per_ebitda_63d_base_v045_signal(prefdivis, ebitda):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis/ebitda mean
def paco_f026_preferred_and_convertible_overhang_per_ebitda_252d_base_v046_signal(prefdivis, ebitda):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis/capex mean
def paco_f026_preferred_and_convertible_overhang_per_capex_63d_base_v047_signal(prefdivis, capex):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis/capex mean
def paco_f026_preferred_and_convertible_overhang_per_capex_252d_base_v048_signal(prefdivis, capex):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d prefdivis/liabilities mean
def paco_f026_preferred_and_convertible_overhang_per_liabilities_63d_base_v049_signal(prefdivis, liabilities):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d prefdivis/liabilities mean
def paco_f026_preferred_and_convertible_overhang_per_liabilities_252d_base_v050_signal(prefdivis, liabilities):
    result = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# prefdivis relative to 252d max times closeadj
def paco_f026_preferred_and_convertible_overhang_relmax_252d_base_v051_signal(prefdivis, closeadj):
    peak = prefdivis.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (prefdivis / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# prefdivis relative to 504d max times closeadj
def paco_f026_preferred_and_convertible_overhang_relmax_504d_base_v052_signal(prefdivis, closeadj):
    peak = prefdivis.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (prefdivis / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# prefdivis relative to 252d min times closeadj
def paco_f026_preferred_and_convertible_overhang_relmin_252d_base_v053_signal(prefdivis, closeadj):
    trough = prefdivis.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (prefdivis / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# prefdivis relative to 504d min times closeadj
def paco_f026_preferred_and_convertible_overhang_relmin_504d_base_v054_signal(prefdivis, closeadj):
    trough = prefdivis.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (prefdivis / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_pct_21d_base_v055_signal(prefdivis, closeadj):
    result = _pct_change(prefdivis, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_pct_63d_base_v056_signal(prefdivis, closeadj):
    result = _pct_change(prefdivis, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_pct_252d_base_v057_signal(prefdivis, closeadj):
    result = _pct_change(prefdivis, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_sum_63d_base_v058_signal(prefdivis, closeadj):
    result = prefdivis.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_sum_252d_base_v059_signal(prefdivis, closeadj):
    result = prefdivis.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_sum_504d_base_v060_signal(prefdivis, closeadj):
    result = prefdivis.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed prefdivis(63d) / smoothed debtusd(252d) x closeadj
def paco_f026_preferred_and_convertible_overhang_rom_debtusd_252_63d_base_v061_signal(prefdivis, debtusd, closeadj):
    n = _mean(prefdivis, 63)
    d = _mean(debtusd, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed prefdivis(126d) / smoothed debtusd(504d) x closeadj
def paco_f026_preferred_and_convertible_overhang_rom_debtusd_504_126d_base_v062_signal(prefdivis, debtusd, closeadj):
    n = _mean(prefdivis, 126)
    d = _mean(debtusd, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed prefdivis(63d) / smoothed assets(252d) x closeadj
def paco_f026_preferred_and_convertible_overhang_rom_assets_252_63d_base_v063_signal(prefdivis, assets, closeadj):
    n = _mean(prefdivis, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed prefdivis(126d) / smoothed assets(504d) x closeadj
def paco_f026_preferred_and_convertible_overhang_rom_assets_504_126d_base_v064_signal(prefdivis, assets, closeadj):
    n = _mean(prefdivis, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed prefdivis(63d) / smoothed marketcap(252d) x closeadj
def paco_f026_preferred_and_convertible_overhang_rom_marketcap_252_63d_base_v065_signal(prefdivis, marketcap, closeadj):
    n = _mean(prefdivis, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed prefdivis(126d) / smoothed marketcap(504d) x closeadj
def paco_f026_preferred_and_convertible_overhang_rom_marketcap_504_126d_base_v066_signal(prefdivis, marketcap, closeadj):
    n = _mean(prefdivis, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(prefdivis) / std(debtusd)
def paco_f026_preferred_and_convertible_overhang_volratio_debtusd_252d_base_v067_signal(prefdivis, debtusd):
    n = _std(prefdivis, 252)
    d = _std(debtusd, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(prefdivis) / std(debtusd)
def paco_f026_preferred_and_convertible_overhang_volratio_debtusd_504d_base_v068_signal(prefdivis, debtusd):
    n = _std(prefdivis, 504)
    d = _std(debtusd, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(prefdivis) / std(assets)
def paco_f026_preferred_and_convertible_overhang_volratio_assets_252d_base_v069_signal(prefdivis, assets):
    n = _std(prefdivis, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(prefdivis) / std(assets)
def paco_f026_preferred_and_convertible_overhang_volratio_assets_504d_base_v070_signal(prefdivis, assets):
    n = _std(prefdivis, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_raw_5d_base_v071_signal(prefdivis, closeadj):
    result = _mean(prefdivis, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_raw_1008d_base_v072_signal(prefdivis, closeadj):
    result = _mean(prefdivis, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of prefdivis/debtusd
def paco_f026_preferred_and_convertible_overhang_log_per_debtusd_252d_base_v073_signal(prefdivis, debtusd):
    s = _preferred_and_convertible_overhang_scaled(prefdivis, debtusd)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of prefdivis/debtusd
def paco_f026_preferred_and_convertible_overhang_log_per_debtusd_504d_base_v074_signal(prefdivis, debtusd):
    s = _preferred_and_convertible_overhang_scaled(prefdivis, debtusd)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of prefdivis/assets
def paco_f026_preferred_and_convertible_overhang_log_per_assets_252d_base_v075_signal(prefdivis, assets):
    s = _preferred_and_convertible_overhang_scaled(prefdivis, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
