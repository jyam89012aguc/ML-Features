"""Family f79 - EV/EBIT EV/EBITDA P/E P/S  (M_Valuation) | base 001-075"""
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
def _standard_multiples_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _standard_multiples_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _standard_multiples_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed evebit times closeadj
def sm_f79_standard_multiples_raw_21d_base_v001_signal(evebit, closeadj):
    result = _mean(evebit, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed evebit times closeadj
def sm_f79_standard_multiples_raw_63d_base_v002_signal(evebit, closeadj):
    result = _mean(evebit, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed evebit times closeadj
def sm_f79_standard_multiples_raw_126d_base_v003_signal(evebit, closeadj):
    result = _mean(evebit, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed evebit times closeadj
def sm_f79_standard_multiples_raw_252d_base_v004_signal(evebit, closeadj):
    result = _mean(evebit, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed evebit times closeadj
def sm_f79_standard_multiples_raw_504d_base_v005_signal(evebit, closeadj):
    result = _mean(evebit, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(evebit) times closeadj
def sm_f79_standard_multiples_log_21d_base_v006_signal(evebit, closeadj):
    result = _mean(_standard_multiples_log(evebit), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(evebit) times closeadj
def sm_f79_standard_multiples_log_63d_base_v007_signal(evebit, closeadj):
    result = _mean(_standard_multiples_log(evebit), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(evebit) times closeadj
def sm_f79_standard_multiples_log_126d_base_v008_signal(evebit, closeadj):
    result = _mean(_standard_multiples_log(evebit), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(evebit) times closeadj
def sm_f79_standard_multiples_log_252d_base_v009_signal(evebit, closeadj):
    result = _mean(_standard_multiples_log(evebit), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(evebit) times closeadj
def sm_f79_standard_multiples_log_504d_base_v010_signal(evebit, closeadj):
    result = _mean(_standard_multiples_log(evebit), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit/assets mean
def sm_f79_standard_multiples_per_assets_63d_base_v011_signal(evebit, assets):
    result = _mean(_standard_multiples_scaled(evebit, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit/assets mean
def sm_f79_standard_multiples_per_assets_252d_base_v012_signal(evebit, assets):
    result = _mean(_standard_multiples_scaled(evebit, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebit/assets mean
def sm_f79_standard_multiples_per_assets_504d_base_v013_signal(evebit, assets):
    result = _mean(_standard_multiples_scaled(evebit, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit/marketcap mean
def sm_f79_standard_multiples_per_marketcap_63d_base_v014_signal(evebit, marketcap):
    result = _mean(_standard_multiples_scaled(evebit, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit/marketcap mean
def sm_f79_standard_multiples_per_marketcap_252d_base_v015_signal(evebit, marketcap):
    result = _mean(_standard_multiples_scaled(evebit, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebit/marketcap mean
def sm_f79_standard_multiples_per_marketcap_504d_base_v016_signal(evebit, marketcap):
    result = _mean(_standard_multiples_scaled(evebit, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit/equity mean
def sm_f79_standard_multiples_per_equity_63d_base_v017_signal(evebit, equity):
    result = _mean(_standard_multiples_scaled(evebit, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit/equity mean
def sm_f79_standard_multiples_per_equity_252d_base_v018_signal(evebit, equity):
    result = _mean(_standard_multiples_scaled(evebit, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebit/equity mean
def sm_f79_standard_multiples_per_equity_504d_base_v019_signal(evebit, equity):
    result = _mean(_standard_multiples_scaled(evebit, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit/debt mean
def sm_f79_standard_multiples_per_debt_63d_base_v020_signal(evebit, debt):
    result = _mean(_standard_multiples_scaled(evebit, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit/debt mean
def sm_f79_standard_multiples_per_debt_252d_base_v021_signal(evebit, debt):
    result = _mean(_standard_multiples_scaled(evebit, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebit/debt mean
def sm_f79_standard_multiples_per_debt_504d_base_v022_signal(evebit, debt):
    result = _mean(_standard_multiples_scaled(evebit, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit/revenue mean
def sm_f79_standard_multiples_per_revenue_63d_base_v023_signal(evebit, revenue):
    result = _mean(_standard_multiples_scaled(evebit, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit/revenue mean
def sm_f79_standard_multiples_per_revenue_252d_base_v024_signal(evebit, revenue):
    result = _mean(_standard_multiples_scaled(evebit, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebit/revenue mean
def sm_f79_standard_multiples_per_revenue_504d_base_v025_signal(evebit, revenue):
    result = _mean(_standard_multiples_scaled(evebit, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d evebit per share times closeadj
def sm_f79_standard_multiples_pershare_21d_base_v026_signal(evebit, sharesbas, closeadj):
    ps = _standard_multiples_per_share(evebit, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit per share times closeadj
def sm_f79_standard_multiples_pershare_63d_base_v027_signal(evebit, sharesbas, closeadj):
    ps = _standard_multiples_per_share(evebit, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebit per share times closeadj
def sm_f79_standard_multiples_pershare_126d_base_v028_signal(evebit, sharesbas, closeadj):
    ps = _standard_multiples_per_share(evebit, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit per share times closeadj
def sm_f79_standard_multiples_pershare_252d_base_v029_signal(evebit, sharesbas, closeadj):
    ps = _standard_multiples_per_share(evebit, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebit per share times closeadj
def sm_f79_standard_multiples_pershare_504d_base_v030_signal(evebit, sharesbas, closeadj):
    ps = _standard_multiples_per_share(evebit, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of evebit times closeadj
def sm_f79_standard_multiples_std_63d_base_v031_signal(evebit, closeadj):
    result = _std(evebit, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of evebit times closeadj
def sm_f79_standard_multiples_std_252d_base_v032_signal(evebit, closeadj):
    result = _std(evebit, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of evebit times closeadj
def sm_f79_standard_multiples_std_504d_base_v033_signal(evebit, closeadj):
    result = _std(evebit, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of evebit
def sm_f79_standard_multiples_z_252d_base_v034_signal(evebit):
    result = _z(evebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of evebit
def sm_f79_standard_multiples_z_504d_base_v035_signal(evebit):
    result = _z(evebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(evebit)
def sm_f79_standard_multiples_logz_252d_base_v036_signal(evebit):
    result = _z(_standard_multiples_log(evebit), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(evebit)
def sm_f79_standard_multiples_logz_504d_base_v037_signal(evebit):
    result = _z(_standard_multiples_log(evebit), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of evebit^2 times closeadj
def sm_f79_standard_multiples_sq_63d_base_v038_signal(evebit, closeadj):
    result = _mean(evebit * evebit, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of evebit^2 times closeadj
def sm_f79_standard_multiples_sq_252d_base_v039_signal(evebit, closeadj):
    result = _mean(evebit * evebit, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(evebit) times closeadj
def sm_f79_standard_multiples_sign_21d_base_v040_signal(evebit, closeadj):
    result = _mean(np.sign(evebit), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(evebit) times closeadj
def sm_f79_standard_multiples_sign_63d_base_v041_signal(evebit, closeadj):
    result = _mean(np.sign(evebit), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(evebit) times closeadj
def sm_f79_standard_multiples_sign_252d_base_v042_signal(evebit, closeadj):
    result = _mean(np.sign(evebit), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit/opex mean
def sm_f79_standard_multiples_per_opex_63d_base_v043_signal(evebit, opex):
    result = _mean(_standard_multiples_scaled(evebit, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit/opex mean
def sm_f79_standard_multiples_per_opex_252d_base_v044_signal(evebit, opex):
    result = _mean(_standard_multiples_scaled(evebit, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit/ebitda mean
def sm_f79_standard_multiples_per_ebitda_63d_base_v045_signal(evebit, ebitda):
    result = _mean(_standard_multiples_scaled(evebit, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit/ebitda mean
def sm_f79_standard_multiples_per_ebitda_252d_base_v046_signal(evebit, ebitda):
    result = _mean(_standard_multiples_scaled(evebit, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit/capex mean
def sm_f79_standard_multiples_per_capex_63d_base_v047_signal(evebit, capex):
    result = _mean(_standard_multiples_scaled(evebit, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit/capex mean
def sm_f79_standard_multiples_per_capex_252d_base_v048_signal(evebit, capex):
    result = _mean(_standard_multiples_scaled(evebit, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit/liabilities mean
def sm_f79_standard_multiples_per_liabilities_63d_base_v049_signal(evebit, liabilities):
    result = _mean(_standard_multiples_scaled(evebit, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit/liabilities mean
def sm_f79_standard_multiples_per_liabilities_252d_base_v050_signal(evebit, liabilities):
    result = _mean(_standard_multiples_scaled(evebit, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# evebit relative to 252d max times closeadj
def sm_f79_standard_multiples_relmax_252d_base_v051_signal(evebit, closeadj):
    peak = evebit.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (evebit / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# evebit relative to 504d max times closeadj
def sm_f79_standard_multiples_relmax_504d_base_v052_signal(evebit, closeadj):
    peak = evebit.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (evebit / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# evebit relative to 252d min times closeadj
def sm_f79_standard_multiples_relmin_252d_base_v053_signal(evebit, closeadj):
    trough = evebit.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (evebit / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# evebit relative to 504d min times closeadj
def sm_f79_standard_multiples_relmin_504d_base_v054_signal(evebit, closeadj):
    trough = evebit.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (evebit / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of evebit times closeadj
def sm_f79_standard_multiples_pct_21d_base_v055_signal(evebit, closeadj):
    result = _pct_change(evebit, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of evebit times closeadj
def sm_f79_standard_multiples_pct_63d_base_v056_signal(evebit, closeadj):
    result = _pct_change(evebit, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of evebit times closeadj
def sm_f79_standard_multiples_pct_252d_base_v057_signal(evebit, closeadj):
    result = _pct_change(evebit, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of evebit times closeadj
def sm_f79_standard_multiples_sum_63d_base_v058_signal(evebit, closeadj):
    result = evebit.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of evebit times closeadj
def sm_f79_standard_multiples_sum_252d_base_v059_signal(evebit, closeadj):
    result = evebit.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of evebit times closeadj
def sm_f79_standard_multiples_sum_504d_base_v060_signal(evebit, closeadj):
    result = evebit.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed evebit(63d) / smoothed assets(252d) x closeadj
def sm_f79_standard_multiples_rom_assets_252_63d_base_v061_signal(evebit, assets, closeadj):
    n = _mean(evebit, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed evebit(126d) / smoothed assets(504d) x closeadj
def sm_f79_standard_multiples_rom_assets_504_126d_base_v062_signal(evebit, assets, closeadj):
    n = _mean(evebit, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed evebit(63d) / smoothed marketcap(252d) x closeadj
def sm_f79_standard_multiples_rom_marketcap_252_63d_base_v063_signal(evebit, marketcap, closeadj):
    n = _mean(evebit, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed evebit(126d) / smoothed marketcap(504d) x closeadj
def sm_f79_standard_multiples_rom_marketcap_504_126d_base_v064_signal(evebit, marketcap, closeadj):
    n = _mean(evebit, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed evebit(63d) / smoothed equity(252d) x closeadj
def sm_f79_standard_multiples_rom_equity_252_63d_base_v065_signal(evebit, equity, closeadj):
    n = _mean(evebit, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed evebit(126d) / smoothed equity(504d) x closeadj
def sm_f79_standard_multiples_rom_equity_504_126d_base_v066_signal(evebit, equity, closeadj):
    n = _mean(evebit, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(evebit) / std(assets)
def sm_f79_standard_multiples_volratio_assets_252d_base_v067_signal(evebit, assets):
    n = _std(evebit, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(evebit) / std(assets)
def sm_f79_standard_multiples_volratio_assets_504d_base_v068_signal(evebit, assets):
    n = _std(evebit, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(evebit) / std(marketcap)
def sm_f79_standard_multiples_volratio_marketcap_252d_base_v069_signal(evebit, marketcap):
    n = _std(evebit, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(evebit) / std(marketcap)
def sm_f79_standard_multiples_volratio_marketcap_504d_base_v070_signal(evebit, marketcap):
    n = _std(evebit, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed evebit times closeadj
def sm_f79_standard_multiples_raw_5d_base_v071_signal(evebit, closeadj):
    result = _mean(evebit, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed evebit times closeadj
def sm_f79_standard_multiples_raw_1008d_base_v072_signal(evebit, closeadj):
    result = _mean(evebit, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of evebit/assets
def sm_f79_standard_multiples_log_per_assets_252d_base_v073_signal(evebit, assets):
    s = _standard_multiples_scaled(evebit, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of evebit/assets
def sm_f79_standard_multiples_log_per_assets_504d_base_v074_signal(evebit, assets):
    s = _standard_multiples_scaled(evebit, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of evebit/marketcap
def sm_f79_standard_multiples_log_per_marketcap_252d_base_v075_signal(evebit, marketcap):
    s = _standard_multiples_scaled(evebit, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
