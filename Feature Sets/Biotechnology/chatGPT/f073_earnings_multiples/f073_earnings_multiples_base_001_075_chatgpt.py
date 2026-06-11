"""Family f073 - Earnings and EBITDA multiples (Valuation Multiples) | Sharadar tables: SF1,DAILY | fields: pe, evebit, evebitda, ebit, ebitda | base 001-075"""
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
def _earnings_multiples_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _earnings_multiples_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _earnings_multiples_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed pe times closeadj
def em_f073_earnings_multiples_raw_21d_base_v001_signal(pe, closeadj):
    result = _mean(pe, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed pe times closeadj
def em_f073_earnings_multiples_raw_63d_base_v002_signal(pe, closeadj):
    result = _mean(pe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed pe times closeadj
def em_f073_earnings_multiples_raw_126d_base_v003_signal(pe, closeadj):
    result = _mean(pe, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed pe times closeadj
def em_f073_earnings_multiples_raw_252d_base_v004_signal(pe, closeadj):
    result = _mean(pe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed pe times closeadj
def em_f073_earnings_multiples_raw_504d_base_v005_signal(pe, closeadj):
    result = _mean(pe, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(pe) times closeadj
def em_f073_earnings_multiples_log_21d_base_v006_signal(pe, closeadj):
    result = _mean(_earnings_multiples_log(pe), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(pe) times closeadj
def em_f073_earnings_multiples_log_63d_base_v007_signal(pe, closeadj):
    result = _mean(_earnings_multiples_log(pe), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(pe) times closeadj
def em_f073_earnings_multiples_log_126d_base_v008_signal(pe, closeadj):
    result = _mean(_earnings_multiples_log(pe), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(pe) times closeadj
def em_f073_earnings_multiples_log_252d_base_v009_signal(pe, closeadj):
    result = _mean(_earnings_multiples_log(pe), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(pe) times closeadj
def em_f073_earnings_multiples_log_504d_base_v010_signal(pe, closeadj):
    result = _mean(_earnings_multiples_log(pe), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe/evebit mean
def em_f073_earnings_multiples_per_evebit_63d_base_v011_signal(pe, evebit):
    result = _mean(_earnings_multiples_scaled(pe, evebit), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe/evebit mean
def em_f073_earnings_multiples_per_evebit_252d_base_v012_signal(pe, evebit):
    result = _mean(_earnings_multiples_scaled(pe, evebit), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pe/evebit mean
def em_f073_earnings_multiples_per_evebit_504d_base_v013_signal(pe, evebit):
    result = _mean(_earnings_multiples_scaled(pe, evebit), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe/evebitda mean
def em_f073_earnings_multiples_per_evebitda_63d_base_v014_signal(pe, evebitda):
    result = _mean(_earnings_multiples_scaled(pe, evebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe/evebitda mean
def em_f073_earnings_multiples_per_evebitda_252d_base_v015_signal(pe, evebitda):
    result = _mean(_earnings_multiples_scaled(pe, evebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pe/evebitda mean
def em_f073_earnings_multiples_per_evebitda_504d_base_v016_signal(pe, evebitda):
    result = _mean(_earnings_multiples_scaled(pe, evebitda), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe/ebit mean
def em_f073_earnings_multiples_per_ebit_63d_base_v017_signal(pe, ebit):
    result = _mean(_earnings_multiples_scaled(pe, ebit), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe/ebit mean
def em_f073_earnings_multiples_per_ebit_252d_base_v018_signal(pe, ebit):
    result = _mean(_earnings_multiples_scaled(pe, ebit), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pe/ebit mean
def em_f073_earnings_multiples_per_ebit_504d_base_v019_signal(pe, ebit):
    result = _mean(_earnings_multiples_scaled(pe, ebit), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe/assets mean
def em_f073_earnings_multiples_per_assets_63d_base_v020_signal(pe, assets):
    result = _mean(_earnings_multiples_scaled(pe, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe/assets mean
def em_f073_earnings_multiples_per_assets_252d_base_v021_signal(pe, assets):
    result = _mean(_earnings_multiples_scaled(pe, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pe/assets mean
def em_f073_earnings_multiples_per_assets_504d_base_v022_signal(pe, assets):
    result = _mean(_earnings_multiples_scaled(pe, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe/marketcap mean
def em_f073_earnings_multiples_per_marketcap_63d_base_v023_signal(pe, marketcap):
    result = _mean(_earnings_multiples_scaled(pe, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe/marketcap mean
def em_f073_earnings_multiples_per_marketcap_252d_base_v024_signal(pe, marketcap):
    result = _mean(_earnings_multiples_scaled(pe, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pe/marketcap mean
def em_f073_earnings_multiples_per_marketcap_504d_base_v025_signal(pe, marketcap):
    result = _mean(_earnings_multiples_scaled(pe, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pe per share times closeadj
def em_f073_earnings_multiples_pershare_21d_base_v026_signal(pe, sharesbas, closeadj):
    ps = _earnings_multiples_per_share(pe, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe per share times closeadj
def em_f073_earnings_multiples_pershare_63d_base_v027_signal(pe, sharesbas, closeadj):
    ps = _earnings_multiples_per_share(pe, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pe per share times closeadj
def em_f073_earnings_multiples_pershare_126d_base_v028_signal(pe, sharesbas, closeadj):
    ps = _earnings_multiples_per_share(pe, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe per share times closeadj
def em_f073_earnings_multiples_pershare_252d_base_v029_signal(pe, sharesbas, closeadj):
    ps = _earnings_multiples_per_share(pe, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pe per share times closeadj
def em_f073_earnings_multiples_pershare_504d_base_v030_signal(pe, sharesbas, closeadj):
    ps = _earnings_multiples_per_share(pe, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of pe times closeadj
def em_f073_earnings_multiples_std_63d_base_v031_signal(pe, closeadj):
    result = _std(pe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of pe times closeadj
def em_f073_earnings_multiples_std_252d_base_v032_signal(pe, closeadj):
    result = _std(pe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of pe times closeadj
def em_f073_earnings_multiples_std_504d_base_v033_signal(pe, closeadj):
    result = _std(pe, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of pe
def em_f073_earnings_multiples_z_252d_base_v034_signal(pe):
    result = _z(pe, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of pe
def em_f073_earnings_multiples_z_504d_base_v035_signal(pe):
    result = _z(pe, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(pe)
def em_f073_earnings_multiples_logz_252d_base_v036_signal(pe):
    result = _z(_earnings_multiples_log(pe), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(pe)
def em_f073_earnings_multiples_logz_504d_base_v037_signal(pe):
    result = _z(_earnings_multiples_log(pe), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of pe^2 times closeadj
def em_f073_earnings_multiples_sq_63d_base_v038_signal(pe, closeadj):
    result = _mean(pe * pe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of pe^2 times closeadj
def em_f073_earnings_multiples_sq_252d_base_v039_signal(pe, closeadj):
    result = _mean(pe * pe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(pe) times closeadj
def em_f073_earnings_multiples_sign_21d_base_v040_signal(pe, closeadj):
    result = _mean(np.sign(pe), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(pe) times closeadj
def em_f073_earnings_multiples_sign_63d_base_v041_signal(pe, closeadj):
    result = _mean(np.sign(pe), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(pe) times closeadj
def em_f073_earnings_multiples_sign_252d_base_v042_signal(pe, closeadj):
    result = _mean(np.sign(pe), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe/opex mean
def em_f073_earnings_multiples_per_opex_63d_base_v043_signal(pe, opex):
    result = _mean(_earnings_multiples_scaled(pe, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe/opex mean
def em_f073_earnings_multiples_per_opex_252d_base_v044_signal(pe, opex):
    result = _mean(_earnings_multiples_scaled(pe, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe/ebitda mean
def em_f073_earnings_multiples_per_ebitda_63d_base_v045_signal(pe, ebitda):
    result = _mean(_earnings_multiples_scaled(pe, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe/ebitda mean
def em_f073_earnings_multiples_per_ebitda_252d_base_v046_signal(pe, ebitda):
    result = _mean(_earnings_multiples_scaled(pe, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe/capex mean
def em_f073_earnings_multiples_per_capex_63d_base_v047_signal(pe, capex):
    result = _mean(_earnings_multiples_scaled(pe, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe/capex mean
def em_f073_earnings_multiples_per_capex_252d_base_v048_signal(pe, capex):
    result = _mean(_earnings_multiples_scaled(pe, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe/liabilities mean
def em_f073_earnings_multiples_per_liabilities_63d_base_v049_signal(pe, liabilities):
    result = _mean(_earnings_multiples_scaled(pe, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe/liabilities mean
def em_f073_earnings_multiples_per_liabilities_252d_base_v050_signal(pe, liabilities):
    result = _mean(_earnings_multiples_scaled(pe, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pe relative to 252d max times closeadj
def em_f073_earnings_multiples_relmax_252d_base_v051_signal(pe, closeadj):
    peak = pe.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (pe / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pe relative to 504d max times closeadj
def em_f073_earnings_multiples_relmax_504d_base_v052_signal(pe, closeadj):
    peak = pe.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (pe / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pe relative to 252d min times closeadj
def em_f073_earnings_multiples_relmin_252d_base_v053_signal(pe, closeadj):
    trough = pe.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (pe / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pe relative to 504d min times closeadj
def em_f073_earnings_multiples_relmin_504d_base_v054_signal(pe, closeadj):
    trough = pe.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (pe / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of pe times closeadj
def em_f073_earnings_multiples_pct_21d_base_v055_signal(pe, closeadj):
    result = _pct_change(pe, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of pe times closeadj
def em_f073_earnings_multiples_pct_63d_base_v056_signal(pe, closeadj):
    result = _pct_change(pe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of pe times closeadj
def em_f073_earnings_multiples_pct_252d_base_v057_signal(pe, closeadj):
    result = _pct_change(pe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of pe times closeadj
def em_f073_earnings_multiples_sum_63d_base_v058_signal(pe, closeadj):
    result = pe.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of pe times closeadj
def em_f073_earnings_multiples_sum_252d_base_v059_signal(pe, closeadj):
    result = pe.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of pe times closeadj
def em_f073_earnings_multiples_sum_504d_base_v060_signal(pe, closeadj):
    result = pe.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pe(63d) / smoothed evebit(252d) x closeadj
def em_f073_earnings_multiples_rom_evebit_252_63d_base_v061_signal(pe, evebit, closeadj):
    n = _mean(pe, 63)
    d = _mean(evebit, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pe(126d) / smoothed evebit(504d) x closeadj
def em_f073_earnings_multiples_rom_evebit_504_126d_base_v062_signal(pe, evebit, closeadj):
    n = _mean(pe, 126)
    d = _mean(evebit, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pe(63d) / smoothed evebitda(252d) x closeadj
def em_f073_earnings_multiples_rom_evebitda_252_63d_base_v063_signal(pe, evebitda, closeadj):
    n = _mean(pe, 63)
    d = _mean(evebitda, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pe(126d) / smoothed evebitda(504d) x closeadj
def em_f073_earnings_multiples_rom_evebitda_504_126d_base_v064_signal(pe, evebitda, closeadj):
    n = _mean(pe, 126)
    d = _mean(evebitda, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pe(63d) / smoothed ebit(252d) x closeadj
def em_f073_earnings_multiples_rom_ebit_252_63d_base_v065_signal(pe, ebit, closeadj):
    n = _mean(pe, 63)
    d = _mean(ebit, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pe(126d) / smoothed ebit(504d) x closeadj
def em_f073_earnings_multiples_rom_ebit_504_126d_base_v066_signal(pe, ebit, closeadj):
    n = _mean(pe, 126)
    d = _mean(ebit, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(pe) / std(evebit)
def em_f073_earnings_multiples_volratio_evebit_252d_base_v067_signal(pe, evebit):
    n = _std(pe, 252)
    d = _std(evebit, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(pe) / std(evebit)
def em_f073_earnings_multiples_volratio_evebit_504d_base_v068_signal(pe, evebit):
    n = _std(pe, 504)
    d = _std(evebit, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(pe) / std(evebitda)
def em_f073_earnings_multiples_volratio_evebitda_252d_base_v069_signal(pe, evebitda):
    n = _std(pe, 252)
    d = _std(evebitda, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(pe) / std(evebitda)
def em_f073_earnings_multiples_volratio_evebitda_504d_base_v070_signal(pe, evebitda):
    n = _std(pe, 504)
    d = _std(evebitda, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed pe times closeadj
def em_f073_earnings_multiples_raw_5d_base_v071_signal(pe, closeadj):
    result = _mean(pe, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed pe times closeadj
def em_f073_earnings_multiples_raw_1008d_base_v072_signal(pe, closeadj):
    result = _mean(pe, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of pe/evebit
def em_f073_earnings_multiples_log_per_evebit_252d_base_v073_signal(pe, evebit):
    s = _earnings_multiples_scaled(pe, evebit)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of pe/evebit
def em_f073_earnings_multiples_log_per_evebit_504d_base_v074_signal(pe, evebit):
    s = _earnings_multiples_scaled(pe, evebit)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of pe/evebitda
def em_f073_earnings_multiples_log_per_evebitda_252d_base_v075_signal(pe, evebitda):
    s = _earnings_multiples_scaled(pe, evebitda)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
