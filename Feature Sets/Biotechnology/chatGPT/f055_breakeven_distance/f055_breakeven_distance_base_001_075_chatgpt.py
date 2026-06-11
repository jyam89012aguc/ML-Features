"""Family f055 - Distance to breakeven (Margins and Profitability) | Sharadar tables: SF1 | fields: netinc, opinc, revenue, opex | base 001-075"""
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
def _breakeven_distance_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _breakeven_distance_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _breakeven_distance_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed netinc times closeadj
def bd_f055_breakeven_distance_raw_21d_base_v001_signal(netinc, closeadj):
    result = _mean(netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed netinc times closeadj
def bd_f055_breakeven_distance_raw_63d_base_v002_signal(netinc, closeadj):
    result = _mean(netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed netinc times closeadj
def bd_f055_breakeven_distance_raw_126d_base_v003_signal(netinc, closeadj):
    result = _mean(netinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed netinc times closeadj
def bd_f055_breakeven_distance_raw_252d_base_v004_signal(netinc, closeadj):
    result = _mean(netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed netinc times closeadj
def bd_f055_breakeven_distance_raw_504d_base_v005_signal(netinc, closeadj):
    result = _mean(netinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(netinc) times closeadj
def bd_f055_breakeven_distance_log_21d_base_v006_signal(netinc, closeadj):
    result = _mean(_breakeven_distance_log(netinc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(netinc) times closeadj
def bd_f055_breakeven_distance_log_63d_base_v007_signal(netinc, closeadj):
    result = _mean(_breakeven_distance_log(netinc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(netinc) times closeadj
def bd_f055_breakeven_distance_log_126d_base_v008_signal(netinc, closeadj):
    result = _mean(_breakeven_distance_log(netinc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(netinc) times closeadj
def bd_f055_breakeven_distance_log_252d_base_v009_signal(netinc, closeadj):
    result = _mean(_breakeven_distance_log(netinc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(netinc) times closeadj
def bd_f055_breakeven_distance_log_504d_base_v010_signal(netinc, closeadj):
    result = _mean(_breakeven_distance_log(netinc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc/opinc mean
def bd_f055_breakeven_distance_per_opinc_63d_base_v011_signal(netinc, opinc):
    result = _mean(_breakeven_distance_scaled(netinc, opinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc/opinc mean
def bd_f055_breakeven_distance_per_opinc_252d_base_v012_signal(netinc, opinc):
    result = _mean(_breakeven_distance_scaled(netinc, opinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netinc/opinc mean
def bd_f055_breakeven_distance_per_opinc_504d_base_v013_signal(netinc, opinc):
    result = _mean(_breakeven_distance_scaled(netinc, opinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc/revenue mean
def bd_f055_breakeven_distance_per_revenue_63d_base_v014_signal(netinc, revenue):
    result = _mean(_breakeven_distance_scaled(netinc, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc/revenue mean
def bd_f055_breakeven_distance_per_revenue_252d_base_v015_signal(netinc, revenue):
    result = _mean(_breakeven_distance_scaled(netinc, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netinc/revenue mean
def bd_f055_breakeven_distance_per_revenue_504d_base_v016_signal(netinc, revenue):
    result = _mean(_breakeven_distance_scaled(netinc, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc/assets mean
def bd_f055_breakeven_distance_per_assets_63d_base_v017_signal(netinc, assets):
    result = _mean(_breakeven_distance_scaled(netinc, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc/assets mean
def bd_f055_breakeven_distance_per_assets_252d_base_v018_signal(netinc, assets):
    result = _mean(_breakeven_distance_scaled(netinc, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netinc/assets mean
def bd_f055_breakeven_distance_per_assets_504d_base_v019_signal(netinc, assets):
    result = _mean(_breakeven_distance_scaled(netinc, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc/marketcap mean
def bd_f055_breakeven_distance_per_marketcap_63d_base_v020_signal(netinc, marketcap):
    result = _mean(_breakeven_distance_scaled(netinc, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc/marketcap mean
def bd_f055_breakeven_distance_per_marketcap_252d_base_v021_signal(netinc, marketcap):
    result = _mean(_breakeven_distance_scaled(netinc, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netinc/marketcap mean
def bd_f055_breakeven_distance_per_marketcap_504d_base_v022_signal(netinc, marketcap):
    result = _mean(_breakeven_distance_scaled(netinc, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc/equity mean
def bd_f055_breakeven_distance_per_equity_63d_base_v023_signal(netinc, equity):
    result = _mean(_breakeven_distance_scaled(netinc, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc/equity mean
def bd_f055_breakeven_distance_per_equity_252d_base_v024_signal(netinc, equity):
    result = _mean(_breakeven_distance_scaled(netinc, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netinc/equity mean
def bd_f055_breakeven_distance_per_equity_504d_base_v025_signal(netinc, equity):
    result = _mean(_breakeven_distance_scaled(netinc, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d netinc per share times closeadj
def bd_f055_breakeven_distance_pershare_21d_base_v026_signal(netinc, sharesbas, closeadj):
    ps = _breakeven_distance_per_share(netinc, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc per share times closeadj
def bd_f055_breakeven_distance_pershare_63d_base_v027_signal(netinc, sharesbas, closeadj):
    ps = _breakeven_distance_per_share(netinc, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d netinc per share times closeadj
def bd_f055_breakeven_distance_pershare_126d_base_v028_signal(netinc, sharesbas, closeadj):
    ps = _breakeven_distance_per_share(netinc, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc per share times closeadj
def bd_f055_breakeven_distance_pershare_252d_base_v029_signal(netinc, sharesbas, closeadj):
    ps = _breakeven_distance_per_share(netinc, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netinc per share times closeadj
def bd_f055_breakeven_distance_pershare_504d_base_v030_signal(netinc, sharesbas, closeadj):
    ps = _breakeven_distance_per_share(netinc, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of netinc times closeadj
def bd_f055_breakeven_distance_std_63d_base_v031_signal(netinc, closeadj):
    result = _std(netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of netinc times closeadj
def bd_f055_breakeven_distance_std_252d_base_v032_signal(netinc, closeadj):
    result = _std(netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of netinc times closeadj
def bd_f055_breakeven_distance_std_504d_base_v033_signal(netinc, closeadj):
    result = _std(netinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of netinc
def bd_f055_breakeven_distance_z_252d_base_v034_signal(netinc):
    result = _z(netinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of netinc
def bd_f055_breakeven_distance_z_504d_base_v035_signal(netinc):
    result = _z(netinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(netinc)
def bd_f055_breakeven_distance_logz_252d_base_v036_signal(netinc):
    result = _z(_breakeven_distance_log(netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(netinc)
def bd_f055_breakeven_distance_logz_504d_base_v037_signal(netinc):
    result = _z(_breakeven_distance_log(netinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of netinc^2 times closeadj
def bd_f055_breakeven_distance_sq_63d_base_v038_signal(netinc, closeadj):
    result = _mean(netinc * netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of netinc^2 times closeadj
def bd_f055_breakeven_distance_sq_252d_base_v039_signal(netinc, closeadj):
    result = _mean(netinc * netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(netinc) times closeadj
def bd_f055_breakeven_distance_sign_21d_base_v040_signal(netinc, closeadj):
    result = _mean(np.sign(netinc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(netinc) times closeadj
def bd_f055_breakeven_distance_sign_63d_base_v041_signal(netinc, closeadj):
    result = _mean(np.sign(netinc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(netinc) times closeadj
def bd_f055_breakeven_distance_sign_252d_base_v042_signal(netinc, closeadj):
    result = _mean(np.sign(netinc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc/opex mean
def bd_f055_breakeven_distance_per_opex_63d_base_v043_signal(netinc, opex):
    result = _mean(_breakeven_distance_scaled(netinc, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc/opex mean
def bd_f055_breakeven_distance_per_opex_252d_base_v044_signal(netinc, opex):
    result = _mean(_breakeven_distance_scaled(netinc, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc/ebitda mean
def bd_f055_breakeven_distance_per_ebitda_63d_base_v045_signal(netinc, ebitda):
    result = _mean(_breakeven_distance_scaled(netinc, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc/ebitda mean
def bd_f055_breakeven_distance_per_ebitda_252d_base_v046_signal(netinc, ebitda):
    result = _mean(_breakeven_distance_scaled(netinc, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc/capex mean
def bd_f055_breakeven_distance_per_capex_63d_base_v047_signal(netinc, capex):
    result = _mean(_breakeven_distance_scaled(netinc, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc/capex mean
def bd_f055_breakeven_distance_per_capex_252d_base_v048_signal(netinc, capex):
    result = _mean(_breakeven_distance_scaled(netinc, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netinc/liabilities mean
def bd_f055_breakeven_distance_per_liabilities_63d_base_v049_signal(netinc, liabilities):
    result = _mean(_breakeven_distance_scaled(netinc, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netinc/liabilities mean
def bd_f055_breakeven_distance_per_liabilities_252d_base_v050_signal(netinc, liabilities):
    result = _mean(_breakeven_distance_scaled(netinc, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# netinc relative to 252d max times closeadj
def bd_f055_breakeven_distance_relmax_252d_base_v051_signal(netinc, closeadj):
    peak = netinc.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (netinc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netinc relative to 504d max times closeadj
def bd_f055_breakeven_distance_relmax_504d_base_v052_signal(netinc, closeadj):
    peak = netinc.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (netinc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netinc relative to 252d min times closeadj
def bd_f055_breakeven_distance_relmin_252d_base_v053_signal(netinc, closeadj):
    trough = netinc.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (netinc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netinc relative to 504d min times closeadj
def bd_f055_breakeven_distance_relmin_504d_base_v054_signal(netinc, closeadj):
    trough = netinc.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (netinc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of netinc times closeadj
def bd_f055_breakeven_distance_pct_21d_base_v055_signal(netinc, closeadj):
    result = _pct_change(netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of netinc times closeadj
def bd_f055_breakeven_distance_pct_63d_base_v056_signal(netinc, closeadj):
    result = _pct_change(netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of netinc times closeadj
def bd_f055_breakeven_distance_pct_252d_base_v057_signal(netinc, closeadj):
    result = _pct_change(netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of netinc times closeadj
def bd_f055_breakeven_distance_sum_63d_base_v058_signal(netinc, closeadj):
    result = netinc.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of netinc times closeadj
def bd_f055_breakeven_distance_sum_252d_base_v059_signal(netinc, closeadj):
    result = netinc.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of netinc times closeadj
def bd_f055_breakeven_distance_sum_504d_base_v060_signal(netinc, closeadj):
    result = netinc.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netinc(63d) / smoothed opinc(252d) x closeadj
def bd_f055_breakeven_distance_rom_opinc_252_63d_base_v061_signal(netinc, opinc, closeadj):
    n = _mean(netinc, 63)
    d = _mean(opinc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netinc(126d) / smoothed opinc(504d) x closeadj
def bd_f055_breakeven_distance_rom_opinc_504_126d_base_v062_signal(netinc, opinc, closeadj):
    n = _mean(netinc, 126)
    d = _mean(opinc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netinc(63d) / smoothed revenue(252d) x closeadj
def bd_f055_breakeven_distance_rom_revenue_252_63d_base_v063_signal(netinc, revenue, closeadj):
    n = _mean(netinc, 63)
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netinc(126d) / smoothed revenue(504d) x closeadj
def bd_f055_breakeven_distance_rom_revenue_504_126d_base_v064_signal(netinc, revenue, closeadj):
    n = _mean(netinc, 126)
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netinc(63d) / smoothed assets(252d) x closeadj
def bd_f055_breakeven_distance_rom_assets_252_63d_base_v065_signal(netinc, assets, closeadj):
    n = _mean(netinc, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netinc(126d) / smoothed assets(504d) x closeadj
def bd_f055_breakeven_distance_rom_assets_504_126d_base_v066_signal(netinc, assets, closeadj):
    n = _mean(netinc, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(netinc) / std(opinc)
def bd_f055_breakeven_distance_volratio_opinc_252d_base_v067_signal(netinc, opinc):
    n = _std(netinc, 252)
    d = _std(opinc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(netinc) / std(opinc)
def bd_f055_breakeven_distance_volratio_opinc_504d_base_v068_signal(netinc, opinc):
    n = _std(netinc, 504)
    d = _std(opinc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(netinc) / std(revenue)
def bd_f055_breakeven_distance_volratio_revenue_252d_base_v069_signal(netinc, revenue):
    n = _std(netinc, 252)
    d = _std(revenue, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(netinc) / std(revenue)
def bd_f055_breakeven_distance_volratio_revenue_504d_base_v070_signal(netinc, revenue):
    n = _std(netinc, 504)
    d = _std(revenue, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed netinc times closeadj
def bd_f055_breakeven_distance_raw_5d_base_v071_signal(netinc, closeadj):
    result = _mean(netinc, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed netinc times closeadj
def bd_f055_breakeven_distance_raw_1008d_base_v072_signal(netinc, closeadj):
    result = _mean(netinc, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of netinc/opinc
def bd_f055_breakeven_distance_log_per_opinc_252d_base_v073_signal(netinc, opinc):
    s = _breakeven_distance_scaled(netinc, opinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of netinc/opinc
def bd_f055_breakeven_distance_log_per_opinc_504d_base_v074_signal(netinc, opinc):
    s = _breakeven_distance_scaled(netinc, opinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of netinc/revenue
def bd_f055_breakeven_distance_log_per_revenue_252d_base_v075_signal(netinc, revenue):
    s = _breakeven_distance_scaled(netinc, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
