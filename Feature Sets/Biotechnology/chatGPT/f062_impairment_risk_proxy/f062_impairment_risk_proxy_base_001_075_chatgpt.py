"""Family f062 - Impairment risk proxy (Earnings and Quality) | Sharadar tables: SF1 | fields: intangibles, depamor, assets, equity | base 001-075"""
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
def _impairment_risk_proxy_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _impairment_risk_proxy_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _impairment_risk_proxy_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed intangibles times closeadj
def irp_f062_impairment_risk_proxy_raw_21d_base_v001_signal(intangibles, closeadj):
    result = _mean(intangibles, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed intangibles times closeadj
def irp_f062_impairment_risk_proxy_raw_63d_base_v002_signal(intangibles, closeadj):
    result = _mean(intangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed intangibles times closeadj
def irp_f062_impairment_risk_proxy_raw_126d_base_v003_signal(intangibles, closeadj):
    result = _mean(intangibles, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed intangibles times closeadj
def irp_f062_impairment_risk_proxy_raw_252d_base_v004_signal(intangibles, closeadj):
    result = _mean(intangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed intangibles times closeadj
def irp_f062_impairment_risk_proxy_raw_504d_base_v005_signal(intangibles, closeadj):
    result = _mean(intangibles, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(intangibles) times closeadj
def irp_f062_impairment_risk_proxy_log_21d_base_v006_signal(intangibles, closeadj):
    result = _mean(_impairment_risk_proxy_log(intangibles), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(intangibles) times closeadj
def irp_f062_impairment_risk_proxy_log_63d_base_v007_signal(intangibles, closeadj):
    result = _mean(_impairment_risk_proxy_log(intangibles), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(intangibles) times closeadj
def irp_f062_impairment_risk_proxy_log_126d_base_v008_signal(intangibles, closeadj):
    result = _mean(_impairment_risk_proxy_log(intangibles), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(intangibles) times closeadj
def irp_f062_impairment_risk_proxy_log_252d_base_v009_signal(intangibles, closeadj):
    result = _mean(_impairment_risk_proxy_log(intangibles), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(intangibles) times closeadj
def irp_f062_impairment_risk_proxy_log_504d_base_v010_signal(intangibles, closeadj):
    result = _mean(_impairment_risk_proxy_log(intangibles), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles/depamor mean
def irp_f062_impairment_risk_proxy_per_depamor_63d_base_v011_signal(intangibles, depamor):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, depamor), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles/depamor mean
def irp_f062_impairment_risk_proxy_per_depamor_252d_base_v012_signal(intangibles, depamor):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, depamor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intangibles/depamor mean
def irp_f062_impairment_risk_proxy_per_depamor_504d_base_v013_signal(intangibles, depamor):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, depamor), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles/assets mean
def irp_f062_impairment_risk_proxy_per_assets_63d_base_v014_signal(intangibles, assets):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles/assets mean
def irp_f062_impairment_risk_proxy_per_assets_252d_base_v015_signal(intangibles, assets):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intangibles/assets mean
def irp_f062_impairment_risk_proxy_per_assets_504d_base_v016_signal(intangibles, assets):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles/equity mean
def irp_f062_impairment_risk_proxy_per_equity_63d_base_v017_signal(intangibles, equity):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles/equity mean
def irp_f062_impairment_risk_proxy_per_equity_252d_base_v018_signal(intangibles, equity):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intangibles/equity mean
def irp_f062_impairment_risk_proxy_per_equity_504d_base_v019_signal(intangibles, equity):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles/equity mean
def irp_f062_impairment_risk_proxy_per_equity_63d_base_v020_signal(intangibles, equity):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles/equity mean
def irp_f062_impairment_risk_proxy_per_equity_252d_base_v021_signal(intangibles, equity):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intangibles/equity mean
def irp_f062_impairment_risk_proxy_per_equity_504d_base_v022_signal(intangibles, equity):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles/debt mean
def irp_f062_impairment_risk_proxy_per_debt_63d_base_v023_signal(intangibles, debt):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles/debt mean
def irp_f062_impairment_risk_proxy_per_debt_252d_base_v024_signal(intangibles, debt):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intangibles/debt mean
def irp_f062_impairment_risk_proxy_per_debt_504d_base_v025_signal(intangibles, debt):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles per share times closeadj
def irp_f062_impairment_risk_proxy_pershare_21d_base_v026_signal(intangibles, sharesbas, closeadj):
    ps = _impairment_risk_proxy_per_share(intangibles, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles per share times closeadj
def irp_f062_impairment_risk_proxy_pershare_63d_base_v027_signal(intangibles, sharesbas, closeadj):
    ps = _impairment_risk_proxy_per_share(intangibles, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d intangibles per share times closeadj
def irp_f062_impairment_risk_proxy_pershare_126d_base_v028_signal(intangibles, sharesbas, closeadj):
    ps = _impairment_risk_proxy_per_share(intangibles, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles per share times closeadj
def irp_f062_impairment_risk_proxy_pershare_252d_base_v029_signal(intangibles, sharesbas, closeadj):
    ps = _impairment_risk_proxy_per_share(intangibles, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intangibles per share times closeadj
def irp_f062_impairment_risk_proxy_pershare_504d_base_v030_signal(intangibles, sharesbas, closeadj):
    ps = _impairment_risk_proxy_per_share(intangibles, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of intangibles times closeadj
def irp_f062_impairment_risk_proxy_std_63d_base_v031_signal(intangibles, closeadj):
    result = _std(intangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of intangibles times closeadj
def irp_f062_impairment_risk_proxy_std_252d_base_v032_signal(intangibles, closeadj):
    result = _std(intangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of intangibles times closeadj
def irp_f062_impairment_risk_proxy_std_504d_base_v033_signal(intangibles, closeadj):
    result = _std(intangibles, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of intangibles
def irp_f062_impairment_risk_proxy_z_252d_base_v034_signal(intangibles):
    result = _z(intangibles, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of intangibles
def irp_f062_impairment_risk_proxy_z_504d_base_v035_signal(intangibles):
    result = _z(intangibles, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(intangibles)
def irp_f062_impairment_risk_proxy_logz_252d_base_v036_signal(intangibles):
    result = _z(_impairment_risk_proxy_log(intangibles), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(intangibles)
def irp_f062_impairment_risk_proxy_logz_504d_base_v037_signal(intangibles):
    result = _z(_impairment_risk_proxy_log(intangibles), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of intangibles^2 times closeadj
def irp_f062_impairment_risk_proxy_sq_63d_base_v038_signal(intangibles, closeadj):
    result = _mean(intangibles * intangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of intangibles^2 times closeadj
def irp_f062_impairment_risk_proxy_sq_252d_base_v039_signal(intangibles, closeadj):
    result = _mean(intangibles * intangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(intangibles) times closeadj
def irp_f062_impairment_risk_proxy_sign_21d_base_v040_signal(intangibles, closeadj):
    result = _mean(np.sign(intangibles), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(intangibles) times closeadj
def irp_f062_impairment_risk_proxy_sign_63d_base_v041_signal(intangibles, closeadj):
    result = _mean(np.sign(intangibles), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(intangibles) times closeadj
def irp_f062_impairment_risk_proxy_sign_252d_base_v042_signal(intangibles, closeadj):
    result = _mean(np.sign(intangibles), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles/opex mean
def irp_f062_impairment_risk_proxy_per_opex_63d_base_v043_signal(intangibles, opex):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles/opex mean
def irp_f062_impairment_risk_proxy_per_opex_252d_base_v044_signal(intangibles, opex):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles/ebitda mean
def irp_f062_impairment_risk_proxy_per_ebitda_63d_base_v045_signal(intangibles, ebitda):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles/ebitda mean
def irp_f062_impairment_risk_proxy_per_ebitda_252d_base_v046_signal(intangibles, ebitda):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles/capex mean
def irp_f062_impairment_risk_proxy_per_capex_63d_base_v047_signal(intangibles, capex):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles/capex mean
def irp_f062_impairment_risk_proxy_per_capex_252d_base_v048_signal(intangibles, capex):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles/liabilities mean
def irp_f062_impairment_risk_proxy_per_liabilities_63d_base_v049_signal(intangibles, liabilities):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles/liabilities mean
def irp_f062_impairment_risk_proxy_per_liabilities_252d_base_v050_signal(intangibles, liabilities):
    result = _mean(_impairment_risk_proxy_scaled(intangibles, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles relative to 252d max times closeadj
def irp_f062_impairment_risk_proxy_relmax_252d_base_v051_signal(intangibles, closeadj):
    peak = intangibles.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (intangibles / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles relative to 504d max times closeadj
def irp_f062_impairment_risk_proxy_relmax_504d_base_v052_signal(intangibles, closeadj):
    peak = intangibles.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (intangibles / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles relative to 252d min times closeadj
def irp_f062_impairment_risk_proxy_relmin_252d_base_v053_signal(intangibles, closeadj):
    trough = intangibles.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (intangibles / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles relative to 504d min times closeadj
def irp_f062_impairment_risk_proxy_relmin_504d_base_v054_signal(intangibles, closeadj):
    trough = intangibles.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (intangibles / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of intangibles times closeadj
def irp_f062_impairment_risk_proxy_pct_21d_base_v055_signal(intangibles, closeadj):
    result = _pct_change(intangibles, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of intangibles times closeadj
def irp_f062_impairment_risk_proxy_pct_63d_base_v056_signal(intangibles, closeadj):
    result = _pct_change(intangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of intangibles times closeadj
def irp_f062_impairment_risk_proxy_pct_252d_base_v057_signal(intangibles, closeadj):
    result = _pct_change(intangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of intangibles times closeadj
def irp_f062_impairment_risk_proxy_sum_63d_base_v058_signal(intangibles, closeadj):
    result = intangibles.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of intangibles times closeadj
def irp_f062_impairment_risk_proxy_sum_252d_base_v059_signal(intangibles, closeadj):
    result = intangibles.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of intangibles times closeadj
def irp_f062_impairment_risk_proxy_sum_504d_base_v060_signal(intangibles, closeadj):
    result = intangibles.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intangibles(63d) / smoothed depamor(252d) x closeadj
def irp_f062_impairment_risk_proxy_rom_depamor_252_63d_base_v061_signal(intangibles, depamor, closeadj):
    n = _mean(intangibles, 63)
    d = _mean(depamor, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intangibles(126d) / smoothed depamor(504d) x closeadj
def irp_f062_impairment_risk_proxy_rom_depamor_504_126d_base_v062_signal(intangibles, depamor, closeadj):
    n = _mean(intangibles, 126)
    d = _mean(depamor, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intangibles(63d) / smoothed assets(252d) x closeadj
def irp_f062_impairment_risk_proxy_rom_assets_252_63d_base_v063_signal(intangibles, assets, closeadj):
    n = _mean(intangibles, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intangibles(126d) / smoothed assets(504d) x closeadj
def irp_f062_impairment_risk_proxy_rom_assets_504_126d_base_v064_signal(intangibles, assets, closeadj):
    n = _mean(intangibles, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intangibles(63d) / smoothed equity(252d) x closeadj
def irp_f062_impairment_risk_proxy_rom_equity_252_63d_base_v065_signal(intangibles, equity, closeadj):
    n = _mean(intangibles, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intangibles(126d) / smoothed equity(504d) x closeadj
def irp_f062_impairment_risk_proxy_rom_equity_504_126d_base_v066_signal(intangibles, equity, closeadj):
    n = _mean(intangibles, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(intangibles) / std(depamor)
def irp_f062_impairment_risk_proxy_volratio_depamor_252d_base_v067_signal(intangibles, depamor):
    n = _std(intangibles, 252)
    d = _std(depamor, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(intangibles) / std(depamor)
def irp_f062_impairment_risk_proxy_volratio_depamor_504d_base_v068_signal(intangibles, depamor):
    n = _std(intangibles, 504)
    d = _std(depamor, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(intangibles) / std(assets)
def irp_f062_impairment_risk_proxy_volratio_assets_252d_base_v069_signal(intangibles, assets):
    n = _std(intangibles, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(intangibles) / std(assets)
def irp_f062_impairment_risk_proxy_volratio_assets_504d_base_v070_signal(intangibles, assets):
    n = _std(intangibles, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed intangibles times closeadj
def irp_f062_impairment_risk_proxy_raw_5d_base_v071_signal(intangibles, closeadj):
    result = _mean(intangibles, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed intangibles times closeadj
def irp_f062_impairment_risk_proxy_raw_1008d_base_v072_signal(intangibles, closeadj):
    result = _mean(intangibles, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of intangibles/depamor
def irp_f062_impairment_risk_proxy_log_per_depamor_252d_base_v073_signal(intangibles, depamor):
    s = _impairment_risk_proxy_scaled(intangibles, depamor)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of intangibles/depamor
def irp_f062_impairment_risk_proxy_log_per_depamor_504d_base_v074_signal(intangibles, depamor):
    s = _impairment_risk_proxy_scaled(intangibles, depamor)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of intangibles/assets
def irp_f062_impairment_risk_proxy_log_per_assets_252d_base_v075_signal(intangibles, assets):
    s = _impairment_risk_proxy_scaled(intangibles, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
