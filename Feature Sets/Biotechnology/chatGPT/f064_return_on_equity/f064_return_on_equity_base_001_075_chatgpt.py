"""Family f064 - Return on equity (Returns and Efficiency) | Sharadar tables: SF1 | fields: roe, netinc, equity | base 001-075"""
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
def _return_on_equity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _return_on_equity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _return_on_equity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed roe times closeadj
def roe_f064_return_on_equity_raw_21d_base_v001_signal(roe, closeadj):
    result = _mean(roe, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed roe times closeadj
def roe_f064_return_on_equity_raw_63d_base_v002_signal(roe, closeadj):
    result = _mean(roe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed roe times closeadj
def roe_f064_return_on_equity_raw_126d_base_v003_signal(roe, closeadj):
    result = _mean(roe, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed roe times closeadj
def roe_f064_return_on_equity_raw_252d_base_v004_signal(roe, closeadj):
    result = _mean(roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed roe times closeadj
def roe_f064_return_on_equity_raw_504d_base_v005_signal(roe, closeadj):
    result = _mean(roe, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(roe) times closeadj
def roe_f064_return_on_equity_log_21d_base_v006_signal(roe, closeadj):
    result = _mean(_return_on_equity_log(roe), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(roe) times closeadj
def roe_f064_return_on_equity_log_63d_base_v007_signal(roe, closeadj):
    result = _mean(_return_on_equity_log(roe), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(roe) times closeadj
def roe_f064_return_on_equity_log_126d_base_v008_signal(roe, closeadj):
    result = _mean(_return_on_equity_log(roe), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(roe) times closeadj
def roe_f064_return_on_equity_log_252d_base_v009_signal(roe, closeadj):
    result = _mean(_return_on_equity_log(roe), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(roe) times closeadj
def roe_f064_return_on_equity_log_504d_base_v010_signal(roe, closeadj):
    result = _mean(_return_on_equity_log(roe), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe/netinc mean
def roe_f064_return_on_equity_per_netinc_63d_base_v011_signal(roe, netinc):
    result = _mean(_return_on_equity_scaled(roe, netinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe/netinc mean
def roe_f064_return_on_equity_per_netinc_252d_base_v012_signal(roe, netinc):
    result = _mean(_return_on_equity_scaled(roe, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roe/netinc mean
def roe_f064_return_on_equity_per_netinc_504d_base_v013_signal(roe, netinc):
    result = _mean(_return_on_equity_scaled(roe, netinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe/equity mean
def roe_f064_return_on_equity_per_equity_63d_base_v014_signal(roe, equity):
    result = _mean(_return_on_equity_scaled(roe, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe/equity mean
def roe_f064_return_on_equity_per_equity_252d_base_v015_signal(roe, equity):
    result = _mean(_return_on_equity_scaled(roe, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roe/equity mean
def roe_f064_return_on_equity_per_equity_504d_base_v016_signal(roe, equity):
    result = _mean(_return_on_equity_scaled(roe, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe/assets mean
def roe_f064_return_on_equity_per_assets_63d_base_v017_signal(roe, assets):
    result = _mean(_return_on_equity_scaled(roe, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe/assets mean
def roe_f064_return_on_equity_per_assets_252d_base_v018_signal(roe, assets):
    result = _mean(_return_on_equity_scaled(roe, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roe/assets mean
def roe_f064_return_on_equity_per_assets_504d_base_v019_signal(roe, assets):
    result = _mean(_return_on_equity_scaled(roe, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe/marketcap mean
def roe_f064_return_on_equity_per_marketcap_63d_base_v020_signal(roe, marketcap):
    result = _mean(_return_on_equity_scaled(roe, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe/marketcap mean
def roe_f064_return_on_equity_per_marketcap_252d_base_v021_signal(roe, marketcap):
    result = _mean(_return_on_equity_scaled(roe, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roe/marketcap mean
def roe_f064_return_on_equity_per_marketcap_504d_base_v022_signal(roe, marketcap):
    result = _mean(_return_on_equity_scaled(roe, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe/debt mean
def roe_f064_return_on_equity_per_debt_63d_base_v023_signal(roe, debt):
    result = _mean(_return_on_equity_scaled(roe, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe/debt mean
def roe_f064_return_on_equity_per_debt_252d_base_v024_signal(roe, debt):
    result = _mean(_return_on_equity_scaled(roe, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roe/debt mean
def roe_f064_return_on_equity_per_debt_504d_base_v025_signal(roe, debt):
    result = _mean(_return_on_equity_scaled(roe, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d roe per share times closeadj
def roe_f064_return_on_equity_pershare_21d_base_v026_signal(roe, sharesbas, closeadj):
    ps = _return_on_equity_per_share(roe, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe per share times closeadj
def roe_f064_return_on_equity_pershare_63d_base_v027_signal(roe, sharesbas, closeadj):
    ps = _return_on_equity_per_share(roe, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d roe per share times closeadj
def roe_f064_return_on_equity_pershare_126d_base_v028_signal(roe, sharesbas, closeadj):
    ps = _return_on_equity_per_share(roe, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe per share times closeadj
def roe_f064_return_on_equity_pershare_252d_base_v029_signal(roe, sharesbas, closeadj):
    ps = _return_on_equity_per_share(roe, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roe per share times closeadj
def roe_f064_return_on_equity_pershare_504d_base_v030_signal(roe, sharesbas, closeadj):
    ps = _return_on_equity_per_share(roe, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of roe times closeadj
def roe_f064_return_on_equity_std_63d_base_v031_signal(roe, closeadj):
    result = _std(roe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of roe times closeadj
def roe_f064_return_on_equity_std_252d_base_v032_signal(roe, closeadj):
    result = _std(roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of roe times closeadj
def roe_f064_return_on_equity_std_504d_base_v033_signal(roe, closeadj):
    result = _std(roe, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of roe
def roe_f064_return_on_equity_z_252d_base_v034_signal(roe):
    result = _z(roe, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of roe
def roe_f064_return_on_equity_z_504d_base_v035_signal(roe):
    result = _z(roe, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(roe)
def roe_f064_return_on_equity_logz_252d_base_v036_signal(roe):
    result = _z(_return_on_equity_log(roe), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(roe)
def roe_f064_return_on_equity_logz_504d_base_v037_signal(roe):
    result = _z(_return_on_equity_log(roe), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of roe^2 times closeadj
def roe_f064_return_on_equity_sq_63d_base_v038_signal(roe, closeadj):
    result = _mean(roe * roe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of roe^2 times closeadj
def roe_f064_return_on_equity_sq_252d_base_v039_signal(roe, closeadj):
    result = _mean(roe * roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(roe) times closeadj
def roe_f064_return_on_equity_sign_21d_base_v040_signal(roe, closeadj):
    result = _mean(np.sign(roe), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(roe) times closeadj
def roe_f064_return_on_equity_sign_63d_base_v041_signal(roe, closeadj):
    result = _mean(np.sign(roe), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(roe) times closeadj
def roe_f064_return_on_equity_sign_252d_base_v042_signal(roe, closeadj):
    result = _mean(np.sign(roe), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe/opex mean
def roe_f064_return_on_equity_per_opex_63d_base_v043_signal(roe, opex):
    result = _mean(_return_on_equity_scaled(roe, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe/opex mean
def roe_f064_return_on_equity_per_opex_252d_base_v044_signal(roe, opex):
    result = _mean(_return_on_equity_scaled(roe, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe/ebitda mean
def roe_f064_return_on_equity_per_ebitda_63d_base_v045_signal(roe, ebitda):
    result = _mean(_return_on_equity_scaled(roe, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe/ebitda mean
def roe_f064_return_on_equity_per_ebitda_252d_base_v046_signal(roe, ebitda):
    result = _mean(_return_on_equity_scaled(roe, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe/capex mean
def roe_f064_return_on_equity_per_capex_63d_base_v047_signal(roe, capex):
    result = _mean(_return_on_equity_scaled(roe, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe/capex mean
def roe_f064_return_on_equity_per_capex_252d_base_v048_signal(roe, capex):
    result = _mean(_return_on_equity_scaled(roe, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe/liabilities mean
def roe_f064_return_on_equity_per_liabilities_63d_base_v049_signal(roe, liabilities):
    result = _mean(_return_on_equity_scaled(roe, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe/liabilities mean
def roe_f064_return_on_equity_per_liabilities_252d_base_v050_signal(roe, liabilities):
    result = _mean(_return_on_equity_scaled(roe, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# roe relative to 252d max times closeadj
def roe_f064_return_on_equity_relmax_252d_base_v051_signal(roe, closeadj):
    peak = roe.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (roe / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roe relative to 504d max times closeadj
def roe_f064_return_on_equity_relmax_504d_base_v052_signal(roe, closeadj):
    peak = roe.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (roe / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roe relative to 252d min times closeadj
def roe_f064_return_on_equity_relmin_252d_base_v053_signal(roe, closeadj):
    trough = roe.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (roe / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roe relative to 504d min times closeadj
def roe_f064_return_on_equity_relmin_504d_base_v054_signal(roe, closeadj):
    trough = roe.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (roe / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of roe times closeadj
def roe_f064_return_on_equity_pct_21d_base_v055_signal(roe, closeadj):
    result = _pct_change(roe, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of roe times closeadj
def roe_f064_return_on_equity_pct_63d_base_v056_signal(roe, closeadj):
    result = _pct_change(roe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of roe times closeadj
def roe_f064_return_on_equity_pct_252d_base_v057_signal(roe, closeadj):
    result = _pct_change(roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of roe times closeadj
def roe_f064_return_on_equity_sum_63d_base_v058_signal(roe, closeadj):
    result = roe.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of roe times closeadj
def roe_f064_return_on_equity_sum_252d_base_v059_signal(roe, closeadj):
    result = roe.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of roe times closeadj
def roe_f064_return_on_equity_sum_504d_base_v060_signal(roe, closeadj):
    result = roe.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roe(63d) / smoothed netinc(252d) x closeadj
def roe_f064_return_on_equity_rom_netinc_252_63d_base_v061_signal(roe, netinc, closeadj):
    n = _mean(roe, 63)
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roe(126d) / smoothed netinc(504d) x closeadj
def roe_f064_return_on_equity_rom_netinc_504_126d_base_v062_signal(roe, netinc, closeadj):
    n = _mean(roe, 126)
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roe(63d) / smoothed equity(252d) x closeadj
def roe_f064_return_on_equity_rom_equity_252_63d_base_v063_signal(roe, equity, closeadj):
    n = _mean(roe, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roe(126d) / smoothed equity(504d) x closeadj
def roe_f064_return_on_equity_rom_equity_504_126d_base_v064_signal(roe, equity, closeadj):
    n = _mean(roe, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roe(63d) / smoothed assets(252d) x closeadj
def roe_f064_return_on_equity_rom_assets_252_63d_base_v065_signal(roe, assets, closeadj):
    n = _mean(roe, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roe(126d) / smoothed assets(504d) x closeadj
def roe_f064_return_on_equity_rom_assets_504_126d_base_v066_signal(roe, assets, closeadj):
    n = _mean(roe, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(roe) / std(netinc)
def roe_f064_return_on_equity_volratio_netinc_252d_base_v067_signal(roe, netinc):
    n = _std(roe, 252)
    d = _std(netinc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(roe) / std(netinc)
def roe_f064_return_on_equity_volratio_netinc_504d_base_v068_signal(roe, netinc):
    n = _std(roe, 504)
    d = _std(netinc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(roe) / std(equity)
def roe_f064_return_on_equity_volratio_equity_252d_base_v069_signal(roe, equity):
    n = _std(roe, 252)
    d = _std(equity, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(roe) / std(equity)
def roe_f064_return_on_equity_volratio_equity_504d_base_v070_signal(roe, equity):
    n = _std(roe, 504)
    d = _std(equity, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed roe times closeadj
def roe_f064_return_on_equity_raw_5d_base_v071_signal(roe, closeadj):
    result = _mean(roe, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed roe times closeadj
def roe_f064_return_on_equity_raw_1008d_base_v072_signal(roe, closeadj):
    result = _mean(roe, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of roe/netinc
def roe_f064_return_on_equity_log_per_netinc_252d_base_v073_signal(roe, netinc):
    s = _return_on_equity_scaled(roe, netinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of roe/netinc
def roe_f064_return_on_equity_log_per_netinc_504d_base_v074_signal(roe, netinc):
    s = _return_on_equity_scaled(roe, netinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of roe/equity
def roe_f064_return_on_equity_log_per_equity_252d_base_v075_signal(roe, equity):
    s = _return_on_equity_scaled(roe, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
