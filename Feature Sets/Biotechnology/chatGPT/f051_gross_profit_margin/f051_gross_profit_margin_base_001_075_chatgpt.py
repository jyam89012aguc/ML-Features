"""Family f051 - Gross profit and gross margin (Margins and Profitability) | Sharadar tables: SF1 | fields: gp, grossmargin, revenue | base 001-075"""
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
def _gross_profit_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _gross_profit_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _gross_profit_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed gp times closeadj
def gpm_f051_gross_profit_margin_raw_21d_base_v001_signal(gp, closeadj):
    result = _mean(gp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed gp times closeadj
def gpm_f051_gross_profit_margin_raw_63d_base_v002_signal(gp, closeadj):
    result = _mean(gp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed gp times closeadj
def gpm_f051_gross_profit_margin_raw_126d_base_v003_signal(gp, closeadj):
    result = _mean(gp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed gp times closeadj
def gpm_f051_gross_profit_margin_raw_252d_base_v004_signal(gp, closeadj):
    result = _mean(gp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed gp times closeadj
def gpm_f051_gross_profit_margin_raw_504d_base_v005_signal(gp, closeadj):
    result = _mean(gp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(gp) times closeadj
def gpm_f051_gross_profit_margin_log_21d_base_v006_signal(gp, closeadj):
    result = _mean(_gross_profit_margin_log(gp), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(gp) times closeadj
def gpm_f051_gross_profit_margin_log_63d_base_v007_signal(gp, closeadj):
    result = _mean(_gross_profit_margin_log(gp), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(gp) times closeadj
def gpm_f051_gross_profit_margin_log_126d_base_v008_signal(gp, closeadj):
    result = _mean(_gross_profit_margin_log(gp), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(gp) times closeadj
def gpm_f051_gross_profit_margin_log_252d_base_v009_signal(gp, closeadj):
    result = _mean(_gross_profit_margin_log(gp), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(gp) times closeadj
def gpm_f051_gross_profit_margin_log_504d_base_v010_signal(gp, closeadj):
    result = _mean(_gross_profit_margin_log(gp), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp/grossmargin mean
def gpm_f051_gross_profit_margin_per_grossmargin_63d_base_v011_signal(gp, grossmargin):
    result = _mean(_gross_profit_margin_scaled(gp, grossmargin), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/grossmargin mean
def gpm_f051_gross_profit_margin_per_grossmargin_252d_base_v012_signal(gp, grossmargin):
    result = _mean(_gross_profit_margin_scaled(gp, grossmargin), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gp/grossmargin mean
def gpm_f051_gross_profit_margin_per_grossmargin_504d_base_v013_signal(gp, grossmargin):
    result = _mean(_gross_profit_margin_scaled(gp, grossmargin), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp/revenue mean
def gpm_f051_gross_profit_margin_per_revenue_63d_base_v014_signal(gp, revenue):
    result = _mean(_gross_profit_margin_scaled(gp, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/revenue mean
def gpm_f051_gross_profit_margin_per_revenue_252d_base_v015_signal(gp, revenue):
    result = _mean(_gross_profit_margin_scaled(gp, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gp/revenue mean
def gpm_f051_gross_profit_margin_per_revenue_504d_base_v016_signal(gp, revenue):
    result = _mean(_gross_profit_margin_scaled(gp, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp/assets mean
def gpm_f051_gross_profit_margin_per_assets_63d_base_v017_signal(gp, assets):
    result = _mean(_gross_profit_margin_scaled(gp, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/assets mean
def gpm_f051_gross_profit_margin_per_assets_252d_base_v018_signal(gp, assets):
    result = _mean(_gross_profit_margin_scaled(gp, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gp/assets mean
def gpm_f051_gross_profit_margin_per_assets_504d_base_v019_signal(gp, assets):
    result = _mean(_gross_profit_margin_scaled(gp, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp/marketcap mean
def gpm_f051_gross_profit_margin_per_marketcap_63d_base_v020_signal(gp, marketcap):
    result = _mean(_gross_profit_margin_scaled(gp, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/marketcap mean
def gpm_f051_gross_profit_margin_per_marketcap_252d_base_v021_signal(gp, marketcap):
    result = _mean(_gross_profit_margin_scaled(gp, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gp/marketcap mean
def gpm_f051_gross_profit_margin_per_marketcap_504d_base_v022_signal(gp, marketcap):
    result = _mean(_gross_profit_margin_scaled(gp, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp/equity mean
def gpm_f051_gross_profit_margin_per_equity_63d_base_v023_signal(gp, equity):
    result = _mean(_gross_profit_margin_scaled(gp, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/equity mean
def gpm_f051_gross_profit_margin_per_equity_252d_base_v024_signal(gp, equity):
    result = _mean(_gross_profit_margin_scaled(gp, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gp/equity mean
def gpm_f051_gross_profit_margin_per_equity_504d_base_v025_signal(gp, equity):
    result = _mean(_gross_profit_margin_scaled(gp, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gp per share times closeadj
def gpm_f051_gross_profit_margin_pershare_21d_base_v026_signal(gp, sharesbas, closeadj):
    ps = _gross_profit_margin_per_share(gp, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp per share times closeadj
def gpm_f051_gross_profit_margin_pershare_63d_base_v027_signal(gp, sharesbas, closeadj):
    ps = _gross_profit_margin_per_share(gp, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gp per share times closeadj
def gpm_f051_gross_profit_margin_pershare_126d_base_v028_signal(gp, sharesbas, closeadj):
    ps = _gross_profit_margin_per_share(gp, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp per share times closeadj
def gpm_f051_gross_profit_margin_pershare_252d_base_v029_signal(gp, sharesbas, closeadj):
    ps = _gross_profit_margin_per_share(gp, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gp per share times closeadj
def gpm_f051_gross_profit_margin_pershare_504d_base_v030_signal(gp, sharesbas, closeadj):
    ps = _gross_profit_margin_per_share(gp, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of gp times closeadj
def gpm_f051_gross_profit_margin_std_63d_base_v031_signal(gp, closeadj):
    result = _std(gp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of gp times closeadj
def gpm_f051_gross_profit_margin_std_252d_base_v032_signal(gp, closeadj):
    result = _std(gp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of gp times closeadj
def gpm_f051_gross_profit_margin_std_504d_base_v033_signal(gp, closeadj):
    result = _std(gp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of gp
def gpm_f051_gross_profit_margin_z_252d_base_v034_signal(gp):
    result = _z(gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of gp
def gpm_f051_gross_profit_margin_z_504d_base_v035_signal(gp):
    result = _z(gp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(gp)
def gpm_f051_gross_profit_margin_logz_252d_base_v036_signal(gp):
    result = _z(_gross_profit_margin_log(gp), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(gp)
def gpm_f051_gross_profit_margin_logz_504d_base_v037_signal(gp):
    result = _z(_gross_profit_margin_log(gp), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of gp^2 times closeadj
def gpm_f051_gross_profit_margin_sq_63d_base_v038_signal(gp, closeadj):
    result = _mean(gp * gp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of gp^2 times closeadj
def gpm_f051_gross_profit_margin_sq_252d_base_v039_signal(gp, closeadj):
    result = _mean(gp * gp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(gp) times closeadj
def gpm_f051_gross_profit_margin_sign_21d_base_v040_signal(gp, closeadj):
    result = _mean(np.sign(gp), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(gp) times closeadj
def gpm_f051_gross_profit_margin_sign_63d_base_v041_signal(gp, closeadj):
    result = _mean(np.sign(gp), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(gp) times closeadj
def gpm_f051_gross_profit_margin_sign_252d_base_v042_signal(gp, closeadj):
    result = _mean(np.sign(gp), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp/opex mean
def gpm_f051_gross_profit_margin_per_opex_63d_base_v043_signal(gp, opex):
    result = _mean(_gross_profit_margin_scaled(gp, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/opex mean
def gpm_f051_gross_profit_margin_per_opex_252d_base_v044_signal(gp, opex):
    result = _mean(_gross_profit_margin_scaled(gp, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp/ebitda mean
def gpm_f051_gross_profit_margin_per_ebitda_63d_base_v045_signal(gp, ebitda):
    result = _mean(_gross_profit_margin_scaled(gp, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/ebitda mean
def gpm_f051_gross_profit_margin_per_ebitda_252d_base_v046_signal(gp, ebitda):
    result = _mean(_gross_profit_margin_scaled(gp, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp/capex mean
def gpm_f051_gross_profit_margin_per_capex_63d_base_v047_signal(gp, capex):
    result = _mean(_gross_profit_margin_scaled(gp, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/capex mean
def gpm_f051_gross_profit_margin_per_capex_252d_base_v048_signal(gp, capex):
    result = _mean(_gross_profit_margin_scaled(gp, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp/liabilities mean
def gpm_f051_gross_profit_margin_per_liabilities_63d_base_v049_signal(gp, liabilities):
    result = _mean(_gross_profit_margin_scaled(gp, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/liabilities mean
def gpm_f051_gross_profit_margin_per_liabilities_252d_base_v050_signal(gp, liabilities):
    result = _mean(_gross_profit_margin_scaled(gp, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gp relative to 252d max times closeadj
def gpm_f051_gross_profit_margin_relmax_252d_base_v051_signal(gp, closeadj):
    peak = gp.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (gp / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gp relative to 504d max times closeadj
def gpm_f051_gross_profit_margin_relmax_504d_base_v052_signal(gp, closeadj):
    peak = gp.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (gp / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gp relative to 252d min times closeadj
def gpm_f051_gross_profit_margin_relmin_252d_base_v053_signal(gp, closeadj):
    trough = gp.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (gp / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gp relative to 504d min times closeadj
def gpm_f051_gross_profit_margin_relmin_504d_base_v054_signal(gp, closeadj):
    trough = gp.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (gp / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of gp times closeadj
def gpm_f051_gross_profit_margin_pct_21d_base_v055_signal(gp, closeadj):
    result = _pct_change(gp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of gp times closeadj
def gpm_f051_gross_profit_margin_pct_63d_base_v056_signal(gp, closeadj):
    result = _pct_change(gp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of gp times closeadj
def gpm_f051_gross_profit_margin_pct_252d_base_v057_signal(gp, closeadj):
    result = _pct_change(gp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of gp times closeadj
def gpm_f051_gross_profit_margin_sum_63d_base_v058_signal(gp, closeadj):
    result = gp.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of gp times closeadj
def gpm_f051_gross_profit_margin_sum_252d_base_v059_signal(gp, closeadj):
    result = gp.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of gp times closeadj
def gpm_f051_gross_profit_margin_sum_504d_base_v060_signal(gp, closeadj):
    result = gp.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gp(63d) / smoothed grossmargin(252d) x closeadj
def gpm_f051_gross_profit_margin_rom_grossmargin_252_63d_base_v061_signal(gp, grossmargin, closeadj):
    n = _mean(gp, 63)
    d = _mean(grossmargin, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gp(126d) / smoothed grossmargin(504d) x closeadj
def gpm_f051_gross_profit_margin_rom_grossmargin_504_126d_base_v062_signal(gp, grossmargin, closeadj):
    n = _mean(gp, 126)
    d = _mean(grossmargin, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gp(63d) / smoothed revenue(252d) x closeadj
def gpm_f051_gross_profit_margin_rom_revenue_252_63d_base_v063_signal(gp, revenue, closeadj):
    n = _mean(gp, 63)
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gp(126d) / smoothed revenue(504d) x closeadj
def gpm_f051_gross_profit_margin_rom_revenue_504_126d_base_v064_signal(gp, revenue, closeadj):
    n = _mean(gp, 126)
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gp(63d) / smoothed assets(252d) x closeadj
def gpm_f051_gross_profit_margin_rom_assets_252_63d_base_v065_signal(gp, assets, closeadj):
    n = _mean(gp, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gp(126d) / smoothed assets(504d) x closeadj
def gpm_f051_gross_profit_margin_rom_assets_504_126d_base_v066_signal(gp, assets, closeadj):
    n = _mean(gp, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(gp) / std(grossmargin)
def gpm_f051_gross_profit_margin_volratio_grossmargin_252d_base_v067_signal(gp, grossmargin):
    n = _std(gp, 252)
    d = _std(grossmargin, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(gp) / std(grossmargin)
def gpm_f051_gross_profit_margin_volratio_grossmargin_504d_base_v068_signal(gp, grossmargin):
    n = _std(gp, 504)
    d = _std(grossmargin, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(gp) / std(revenue)
def gpm_f051_gross_profit_margin_volratio_revenue_252d_base_v069_signal(gp, revenue):
    n = _std(gp, 252)
    d = _std(revenue, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(gp) / std(revenue)
def gpm_f051_gross_profit_margin_volratio_revenue_504d_base_v070_signal(gp, revenue):
    n = _std(gp, 504)
    d = _std(revenue, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed gp times closeadj
def gpm_f051_gross_profit_margin_raw_5d_base_v071_signal(gp, closeadj):
    result = _mean(gp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed gp times closeadj
def gpm_f051_gross_profit_margin_raw_1008d_base_v072_signal(gp, closeadj):
    result = _mean(gp, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of gp/grossmargin
def gpm_f051_gross_profit_margin_log_per_grossmargin_252d_base_v073_signal(gp, grossmargin):
    s = _gross_profit_margin_scaled(gp, grossmargin)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of gp/grossmargin
def gpm_f051_gross_profit_margin_log_per_grossmargin_504d_base_v074_signal(gp, grossmargin):
    s = _gross_profit_margin_scaled(gp, grossmargin)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of gp/revenue
def gpm_f051_gross_profit_margin_log_per_revenue_252d_base_v075_signal(gp, revenue):
    s = _gross_profit_margin_scaled(gp, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
