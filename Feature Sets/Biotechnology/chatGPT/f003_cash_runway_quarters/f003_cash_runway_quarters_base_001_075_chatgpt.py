"""Family f003 - Burn-adjusted runway (Liquidity and Runway) | Sharadar tables: SF1 | fields: cashneq, investmentsc, ncfo, fcf | base 001-075"""
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
def _cash_runway_quarters_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _cash_runway_quarters_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _cash_runway_quarters_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed cashneq times closeadj
def crq_f003_cash_runway_quarters_raw_21d_base_v001_signal(cashneq, closeadj):
    result = _mean(cashneq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed cashneq times closeadj
def crq_f003_cash_runway_quarters_raw_63d_base_v002_signal(cashneq, closeadj):
    result = _mean(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed cashneq times closeadj
def crq_f003_cash_runway_quarters_raw_126d_base_v003_signal(cashneq, closeadj):
    result = _mean(cashneq, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed cashneq times closeadj
def crq_f003_cash_runway_quarters_raw_252d_base_v004_signal(cashneq, closeadj):
    result = _mean(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed cashneq times closeadj
def crq_f003_cash_runway_quarters_raw_504d_base_v005_signal(cashneq, closeadj):
    result = _mean(cashneq, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(cashneq) times closeadj
def crq_f003_cash_runway_quarters_log_21d_base_v006_signal(cashneq, closeadj):
    result = _mean(_cash_runway_quarters_log(cashneq), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(cashneq) times closeadj
def crq_f003_cash_runway_quarters_log_63d_base_v007_signal(cashneq, closeadj):
    result = _mean(_cash_runway_quarters_log(cashneq), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(cashneq) times closeadj
def crq_f003_cash_runway_quarters_log_126d_base_v008_signal(cashneq, closeadj):
    result = _mean(_cash_runway_quarters_log(cashneq), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(cashneq) times closeadj
def crq_f003_cash_runway_quarters_log_252d_base_v009_signal(cashneq, closeadj):
    result = _mean(_cash_runway_quarters_log(cashneq), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(cashneq) times closeadj
def crq_f003_cash_runway_quarters_log_504d_base_v010_signal(cashneq, closeadj):
    result = _mean(_cash_runway_quarters_log(cashneq), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/investmentsc mean
def crq_f003_cash_runway_quarters_per_investmentsc_63d_base_v011_signal(cashneq, investmentsc):
    result = _mean(_cash_runway_quarters_scaled(cashneq, investmentsc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/investmentsc mean
def crq_f003_cash_runway_quarters_per_investmentsc_252d_base_v012_signal(cashneq, investmentsc):
    result = _mean(_cash_runway_quarters_scaled(cashneq, investmentsc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/investmentsc mean
def crq_f003_cash_runway_quarters_per_investmentsc_504d_base_v013_signal(cashneq, investmentsc):
    result = _mean(_cash_runway_quarters_scaled(cashneq, investmentsc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/ncfo mean
def crq_f003_cash_runway_quarters_per_ncfo_63d_base_v014_signal(cashneq, ncfo):
    result = _mean(_cash_runway_quarters_scaled(cashneq, ncfo), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/ncfo mean
def crq_f003_cash_runway_quarters_per_ncfo_252d_base_v015_signal(cashneq, ncfo):
    result = _mean(_cash_runway_quarters_scaled(cashneq, ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/ncfo mean
def crq_f003_cash_runway_quarters_per_ncfo_504d_base_v016_signal(cashneq, ncfo):
    result = _mean(_cash_runway_quarters_scaled(cashneq, ncfo), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/fcf mean
def crq_f003_cash_runway_quarters_per_fcf_63d_base_v017_signal(cashneq, fcf):
    result = _mean(_cash_runway_quarters_scaled(cashneq, fcf), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/fcf mean
def crq_f003_cash_runway_quarters_per_fcf_252d_base_v018_signal(cashneq, fcf):
    result = _mean(_cash_runway_quarters_scaled(cashneq, fcf), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/fcf mean
def crq_f003_cash_runway_quarters_per_fcf_504d_base_v019_signal(cashneq, fcf):
    result = _mean(_cash_runway_quarters_scaled(cashneq, fcf), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/assets mean
def crq_f003_cash_runway_quarters_per_assets_63d_base_v020_signal(cashneq, assets):
    result = _mean(_cash_runway_quarters_scaled(cashneq, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/assets mean
def crq_f003_cash_runway_quarters_per_assets_252d_base_v021_signal(cashneq, assets):
    result = _mean(_cash_runway_quarters_scaled(cashneq, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/assets mean
def crq_f003_cash_runway_quarters_per_assets_504d_base_v022_signal(cashneq, assets):
    result = _mean(_cash_runway_quarters_scaled(cashneq, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/marketcap mean
def crq_f003_cash_runway_quarters_per_marketcap_63d_base_v023_signal(cashneq, marketcap):
    result = _mean(_cash_runway_quarters_scaled(cashneq, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/marketcap mean
def crq_f003_cash_runway_quarters_per_marketcap_252d_base_v024_signal(cashneq, marketcap):
    result = _mean(_cash_runway_quarters_scaled(cashneq, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/marketcap mean
def crq_f003_cash_runway_quarters_per_marketcap_504d_base_v025_signal(cashneq, marketcap):
    result = _mean(_cash_runway_quarters_scaled(cashneq, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cashneq per share times closeadj
def crq_f003_cash_runway_quarters_pershare_21d_base_v026_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_quarters_per_share(cashneq, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq per share times closeadj
def crq_f003_cash_runway_quarters_pershare_63d_base_v027_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_quarters_per_share(cashneq, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cashneq per share times closeadj
def crq_f003_cash_runway_quarters_pershare_126d_base_v028_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_quarters_per_share(cashneq, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq per share times closeadj
def crq_f003_cash_runway_quarters_pershare_252d_base_v029_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_quarters_per_share(cashneq, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq per share times closeadj
def crq_f003_cash_runway_quarters_pershare_504d_base_v030_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_quarters_per_share(cashneq, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of cashneq times closeadj
def crq_f003_cash_runway_quarters_std_63d_base_v031_signal(cashneq, closeadj):
    result = _std(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of cashneq times closeadj
def crq_f003_cash_runway_quarters_std_252d_base_v032_signal(cashneq, closeadj):
    result = _std(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of cashneq times closeadj
def crq_f003_cash_runway_quarters_std_504d_base_v033_signal(cashneq, closeadj):
    result = _std(cashneq, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of cashneq
def crq_f003_cash_runway_quarters_z_252d_base_v034_signal(cashneq):
    result = _z(cashneq, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of cashneq
def crq_f003_cash_runway_quarters_z_504d_base_v035_signal(cashneq):
    result = _z(cashneq, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(cashneq)
def crq_f003_cash_runway_quarters_logz_252d_base_v036_signal(cashneq):
    result = _z(_cash_runway_quarters_log(cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(cashneq)
def crq_f003_cash_runway_quarters_logz_504d_base_v037_signal(cashneq):
    result = _z(_cash_runway_quarters_log(cashneq), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of cashneq^2 times closeadj
def crq_f003_cash_runway_quarters_sq_63d_base_v038_signal(cashneq, closeadj):
    result = _mean(cashneq * cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of cashneq^2 times closeadj
def crq_f003_cash_runway_quarters_sq_252d_base_v039_signal(cashneq, closeadj):
    result = _mean(cashneq * cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(cashneq) times closeadj
def crq_f003_cash_runway_quarters_sign_21d_base_v040_signal(cashneq, closeadj):
    result = _mean(np.sign(cashneq), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(cashneq) times closeadj
def crq_f003_cash_runway_quarters_sign_63d_base_v041_signal(cashneq, closeadj):
    result = _mean(np.sign(cashneq), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(cashneq) times closeadj
def crq_f003_cash_runway_quarters_sign_252d_base_v042_signal(cashneq, closeadj):
    result = _mean(np.sign(cashneq), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/opex mean
def crq_f003_cash_runway_quarters_per_opex_63d_base_v043_signal(cashneq, opex):
    result = _mean(_cash_runway_quarters_scaled(cashneq, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/opex mean
def crq_f003_cash_runway_quarters_per_opex_252d_base_v044_signal(cashneq, opex):
    result = _mean(_cash_runway_quarters_scaled(cashneq, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/ebitda mean
def crq_f003_cash_runway_quarters_per_ebitda_63d_base_v045_signal(cashneq, ebitda):
    result = _mean(_cash_runway_quarters_scaled(cashneq, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/ebitda mean
def crq_f003_cash_runway_quarters_per_ebitda_252d_base_v046_signal(cashneq, ebitda):
    result = _mean(_cash_runway_quarters_scaled(cashneq, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/capex mean
def crq_f003_cash_runway_quarters_per_capex_63d_base_v047_signal(cashneq, capex):
    result = _mean(_cash_runway_quarters_scaled(cashneq, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/capex mean
def crq_f003_cash_runway_quarters_per_capex_252d_base_v048_signal(cashneq, capex):
    result = _mean(_cash_runway_quarters_scaled(cashneq, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/liabilities mean
def crq_f003_cash_runway_quarters_per_liabilities_63d_base_v049_signal(cashneq, liabilities):
    result = _mean(_cash_runway_quarters_scaled(cashneq, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/liabilities mean
def crq_f003_cash_runway_quarters_per_liabilities_252d_base_v050_signal(cashneq, liabilities):
    result = _mean(_cash_runway_quarters_scaled(cashneq, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 252d max times closeadj
def crq_f003_cash_runway_quarters_relmax_252d_base_v051_signal(cashneq, closeadj):
    peak = cashneq.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (cashneq / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 504d max times closeadj
def crq_f003_cash_runway_quarters_relmax_504d_base_v052_signal(cashneq, closeadj):
    peak = cashneq.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (cashneq / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 252d min times closeadj
def crq_f003_cash_runway_quarters_relmin_252d_base_v053_signal(cashneq, closeadj):
    trough = cashneq.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (cashneq / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 504d min times closeadj
def crq_f003_cash_runway_quarters_relmin_504d_base_v054_signal(cashneq, closeadj):
    trough = cashneq.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (cashneq / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of cashneq times closeadj
def crq_f003_cash_runway_quarters_pct_21d_base_v055_signal(cashneq, closeadj):
    result = _pct_change(cashneq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of cashneq times closeadj
def crq_f003_cash_runway_quarters_pct_63d_base_v056_signal(cashneq, closeadj):
    result = _pct_change(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of cashneq times closeadj
def crq_f003_cash_runway_quarters_pct_252d_base_v057_signal(cashneq, closeadj):
    result = _pct_change(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of cashneq times closeadj
def crq_f003_cash_runway_quarters_sum_63d_base_v058_signal(cashneq, closeadj):
    result = cashneq.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of cashneq times closeadj
def crq_f003_cash_runway_quarters_sum_252d_base_v059_signal(cashneq, closeadj):
    result = cashneq.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of cashneq times closeadj
def crq_f003_cash_runway_quarters_sum_504d_base_v060_signal(cashneq, closeadj):
    result = cashneq.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(63d) / smoothed investmentsc(252d) x closeadj
def crq_f003_cash_runway_quarters_rom_investmentsc_252_63d_base_v061_signal(cashneq, investmentsc, closeadj):
    n = _mean(cashneq, 63)
    d = _mean(investmentsc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(126d) / smoothed investmentsc(504d) x closeadj
def crq_f003_cash_runway_quarters_rom_investmentsc_504_126d_base_v062_signal(cashneq, investmentsc, closeadj):
    n = _mean(cashneq, 126)
    d = _mean(investmentsc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(63d) / smoothed ncfo(252d) x closeadj
def crq_f003_cash_runway_quarters_rom_ncfo_252_63d_base_v063_signal(cashneq, ncfo, closeadj):
    n = _mean(cashneq, 63)
    d = _mean(ncfo, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(126d) / smoothed ncfo(504d) x closeadj
def crq_f003_cash_runway_quarters_rom_ncfo_504_126d_base_v064_signal(cashneq, ncfo, closeadj):
    n = _mean(cashneq, 126)
    d = _mean(ncfo, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(63d) / smoothed fcf(252d) x closeadj
def crq_f003_cash_runway_quarters_rom_fcf_252_63d_base_v065_signal(cashneq, fcf, closeadj):
    n = _mean(cashneq, 63)
    d = _mean(fcf, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(126d) / smoothed fcf(504d) x closeadj
def crq_f003_cash_runway_quarters_rom_fcf_504_126d_base_v066_signal(cashneq, fcf, closeadj):
    n = _mean(cashneq, 126)
    d = _mean(fcf, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(cashneq) / std(investmentsc)
def crq_f003_cash_runway_quarters_volratio_investmentsc_252d_base_v067_signal(cashneq, investmentsc):
    n = _std(cashneq, 252)
    d = _std(investmentsc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(cashneq) / std(investmentsc)
def crq_f003_cash_runway_quarters_volratio_investmentsc_504d_base_v068_signal(cashneq, investmentsc):
    n = _std(cashneq, 504)
    d = _std(investmentsc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(cashneq) / std(ncfo)
def crq_f003_cash_runway_quarters_volratio_ncfo_252d_base_v069_signal(cashneq, ncfo):
    n = _std(cashneq, 252)
    d = _std(ncfo, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(cashneq) / std(ncfo)
def crq_f003_cash_runway_quarters_volratio_ncfo_504d_base_v070_signal(cashneq, ncfo):
    n = _std(cashneq, 504)
    d = _std(ncfo, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed cashneq times closeadj
def crq_f003_cash_runway_quarters_raw_5d_base_v071_signal(cashneq, closeadj):
    result = _mean(cashneq, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed cashneq times closeadj
def crq_f003_cash_runway_quarters_raw_1008d_base_v072_signal(cashneq, closeadj):
    result = _mean(cashneq, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of cashneq/investmentsc
def crq_f003_cash_runway_quarters_log_per_investmentsc_252d_base_v073_signal(cashneq, investmentsc):
    s = _cash_runway_quarters_scaled(cashneq, investmentsc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of cashneq/investmentsc
def crq_f003_cash_runway_quarters_log_per_investmentsc_504d_base_v074_signal(cashneq, investmentsc):
    s = _cash_runway_quarters_scaled(cashneq, investmentsc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of cashneq/ncfo
def crq_f003_cash_runway_quarters_log_per_ncfo_252d_base_v075_signal(cashneq, ncfo):
    s = _cash_runway_quarters_scaled(cashneq, ncfo)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
