"""Family f76 - EV / R&D  (M_Valuation) | base 001-075"""
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
def _ev_rnd_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ev_rnd_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ev_rnd_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed ev times closeadj
def evd_f76_ev_rnd_raw_21d_base_v001_signal(ev, closeadj):
    result = _mean(ev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed ev times closeadj
def evd_f76_ev_rnd_raw_63d_base_v002_signal(ev, closeadj):
    result = _mean(ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed ev times closeadj
def evd_f76_ev_rnd_raw_126d_base_v003_signal(ev, closeadj):
    result = _mean(ev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed ev times closeadj
def evd_f76_ev_rnd_raw_252d_base_v004_signal(ev, closeadj):
    result = _mean(ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed ev times closeadj
def evd_f76_ev_rnd_raw_504d_base_v005_signal(ev, closeadj):
    result = _mean(ev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(ev) times closeadj
def evd_f76_ev_rnd_log_21d_base_v006_signal(ev, closeadj):
    result = _mean(_ev_rnd_log(ev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(ev) times closeadj
def evd_f76_ev_rnd_log_63d_base_v007_signal(ev, closeadj):
    result = _mean(_ev_rnd_log(ev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(ev) times closeadj
def evd_f76_ev_rnd_log_126d_base_v008_signal(ev, closeadj):
    result = _mean(_ev_rnd_log(ev), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(ev) times closeadj
def evd_f76_ev_rnd_log_252d_base_v009_signal(ev, closeadj):
    result = _mean(_ev_rnd_log(ev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(ev) times closeadj
def evd_f76_ev_rnd_log_504d_base_v010_signal(ev, closeadj):
    result = _mean(_ev_rnd_log(ev), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/assets mean
def evd_f76_ev_rnd_per_assets_63d_base_v011_signal(ev, assets):
    result = _mean(_ev_rnd_scaled(ev, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/assets mean
def evd_f76_ev_rnd_per_assets_252d_base_v012_signal(ev, assets):
    result = _mean(_ev_rnd_scaled(ev, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev/assets mean
def evd_f76_ev_rnd_per_assets_504d_base_v013_signal(ev, assets):
    result = _mean(_ev_rnd_scaled(ev, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/marketcap mean
def evd_f76_ev_rnd_per_marketcap_63d_base_v014_signal(ev, marketcap):
    result = _mean(_ev_rnd_scaled(ev, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/marketcap mean
def evd_f76_ev_rnd_per_marketcap_252d_base_v015_signal(ev, marketcap):
    result = _mean(_ev_rnd_scaled(ev, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev/marketcap mean
def evd_f76_ev_rnd_per_marketcap_504d_base_v016_signal(ev, marketcap):
    result = _mean(_ev_rnd_scaled(ev, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/equity mean
def evd_f76_ev_rnd_per_equity_63d_base_v017_signal(ev, equity):
    result = _mean(_ev_rnd_scaled(ev, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/equity mean
def evd_f76_ev_rnd_per_equity_252d_base_v018_signal(ev, equity):
    result = _mean(_ev_rnd_scaled(ev, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev/equity mean
def evd_f76_ev_rnd_per_equity_504d_base_v019_signal(ev, equity):
    result = _mean(_ev_rnd_scaled(ev, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/debt mean
def evd_f76_ev_rnd_per_debt_63d_base_v020_signal(ev, debt):
    result = _mean(_ev_rnd_scaled(ev, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/debt mean
def evd_f76_ev_rnd_per_debt_252d_base_v021_signal(ev, debt):
    result = _mean(_ev_rnd_scaled(ev, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev/debt mean
def evd_f76_ev_rnd_per_debt_504d_base_v022_signal(ev, debt):
    result = _mean(_ev_rnd_scaled(ev, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/revenue mean
def evd_f76_ev_rnd_per_revenue_63d_base_v023_signal(ev, revenue):
    result = _mean(_ev_rnd_scaled(ev, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/revenue mean
def evd_f76_ev_rnd_per_revenue_252d_base_v024_signal(ev, revenue):
    result = _mean(_ev_rnd_scaled(ev, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev/revenue mean
def evd_f76_ev_rnd_per_revenue_504d_base_v025_signal(ev, revenue):
    result = _mean(_ev_rnd_scaled(ev, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev per share times closeadj
def evd_f76_ev_rnd_pershare_21d_base_v026_signal(ev, sharesbas, closeadj):
    ps = _ev_rnd_per_share(ev, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev per share times closeadj
def evd_f76_ev_rnd_pershare_63d_base_v027_signal(ev, sharesbas, closeadj):
    ps = _ev_rnd_per_share(ev, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev per share times closeadj
def evd_f76_ev_rnd_pershare_126d_base_v028_signal(ev, sharesbas, closeadj):
    ps = _ev_rnd_per_share(ev, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev per share times closeadj
def evd_f76_ev_rnd_pershare_252d_base_v029_signal(ev, sharesbas, closeadj):
    ps = _ev_rnd_per_share(ev, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev per share times closeadj
def evd_f76_ev_rnd_pershare_504d_base_v030_signal(ev, sharesbas, closeadj):
    ps = _ev_rnd_per_share(ev, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of ev times closeadj
def evd_f76_ev_rnd_std_63d_base_v031_signal(ev, closeadj):
    result = _std(ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of ev times closeadj
def evd_f76_ev_rnd_std_252d_base_v032_signal(ev, closeadj):
    result = _std(ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of ev times closeadj
def evd_f76_ev_rnd_std_504d_base_v033_signal(ev, closeadj):
    result = _std(ev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ev
def evd_f76_ev_rnd_z_252d_base_v034_signal(ev):
    result = _z(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ev
def evd_f76_ev_rnd_z_504d_base_v035_signal(ev):
    result = _z(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(ev)
def evd_f76_ev_rnd_logz_252d_base_v036_signal(ev):
    result = _z(_ev_rnd_log(ev), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(ev)
def evd_f76_ev_rnd_logz_504d_base_v037_signal(ev):
    result = _z(_ev_rnd_log(ev), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of ev^2 times closeadj
def evd_f76_ev_rnd_sq_63d_base_v038_signal(ev, closeadj):
    result = _mean(ev * ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of ev^2 times closeadj
def evd_f76_ev_rnd_sq_252d_base_v039_signal(ev, closeadj):
    result = _mean(ev * ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(ev) times closeadj
def evd_f76_ev_rnd_sign_21d_base_v040_signal(ev, closeadj):
    result = _mean(np.sign(ev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(ev) times closeadj
def evd_f76_ev_rnd_sign_63d_base_v041_signal(ev, closeadj):
    result = _mean(np.sign(ev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(ev) times closeadj
def evd_f76_ev_rnd_sign_252d_base_v042_signal(ev, closeadj):
    result = _mean(np.sign(ev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/opex mean
def evd_f76_ev_rnd_per_opex_63d_base_v043_signal(ev, opex):
    result = _mean(_ev_rnd_scaled(ev, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/opex mean
def evd_f76_ev_rnd_per_opex_252d_base_v044_signal(ev, opex):
    result = _mean(_ev_rnd_scaled(ev, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/ebitda mean
def evd_f76_ev_rnd_per_ebitda_63d_base_v045_signal(ev, ebitda):
    result = _mean(_ev_rnd_scaled(ev, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/ebitda mean
def evd_f76_ev_rnd_per_ebitda_252d_base_v046_signal(ev, ebitda):
    result = _mean(_ev_rnd_scaled(ev, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/capex mean
def evd_f76_ev_rnd_per_capex_63d_base_v047_signal(ev, capex):
    result = _mean(_ev_rnd_scaled(ev, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/capex mean
def evd_f76_ev_rnd_per_capex_252d_base_v048_signal(ev, capex):
    result = _mean(_ev_rnd_scaled(ev, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/liabilities mean
def evd_f76_ev_rnd_per_liabilities_63d_base_v049_signal(ev, liabilities):
    result = _mean(_ev_rnd_scaled(ev, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/liabilities mean
def evd_f76_ev_rnd_per_liabilities_252d_base_v050_signal(ev, liabilities):
    result = _mean(_ev_rnd_scaled(ev, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ev relative to 252d max times closeadj
def evd_f76_ev_rnd_relmax_252d_base_v051_signal(ev, closeadj):
    peak = ev.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (ev / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ev relative to 504d max times closeadj
def evd_f76_ev_rnd_relmax_504d_base_v052_signal(ev, closeadj):
    peak = ev.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (ev / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ev relative to 252d min times closeadj
def evd_f76_ev_rnd_relmin_252d_base_v053_signal(ev, closeadj):
    trough = ev.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (ev / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ev relative to 504d min times closeadj
def evd_f76_ev_rnd_relmin_504d_base_v054_signal(ev, closeadj):
    trough = ev.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (ev / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of ev times closeadj
def evd_f76_ev_rnd_pct_21d_base_v055_signal(ev, closeadj):
    result = _pct_change(ev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of ev times closeadj
def evd_f76_ev_rnd_pct_63d_base_v056_signal(ev, closeadj):
    result = _pct_change(ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of ev times closeadj
def evd_f76_ev_rnd_pct_252d_base_v057_signal(ev, closeadj):
    result = _pct_change(ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of ev times closeadj
def evd_f76_ev_rnd_sum_63d_base_v058_signal(ev, closeadj):
    result = ev.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of ev times closeadj
def evd_f76_ev_rnd_sum_252d_base_v059_signal(ev, closeadj):
    result = ev.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of ev times closeadj
def evd_f76_ev_rnd_sum_504d_base_v060_signal(ev, closeadj):
    result = ev.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ev(63d) / smoothed assets(252d) x closeadj
def evd_f76_ev_rnd_rom_assets_252_63d_base_v061_signal(ev, assets, closeadj):
    n = _mean(ev, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ev(126d) / smoothed assets(504d) x closeadj
def evd_f76_ev_rnd_rom_assets_504_126d_base_v062_signal(ev, assets, closeadj):
    n = _mean(ev, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ev(63d) / smoothed marketcap(252d) x closeadj
def evd_f76_ev_rnd_rom_marketcap_252_63d_base_v063_signal(ev, marketcap, closeadj):
    n = _mean(ev, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ev(126d) / smoothed marketcap(504d) x closeadj
def evd_f76_ev_rnd_rom_marketcap_504_126d_base_v064_signal(ev, marketcap, closeadj):
    n = _mean(ev, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ev(63d) / smoothed equity(252d) x closeadj
def evd_f76_ev_rnd_rom_equity_252_63d_base_v065_signal(ev, equity, closeadj):
    n = _mean(ev, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ev(126d) / smoothed equity(504d) x closeadj
def evd_f76_ev_rnd_rom_equity_504_126d_base_v066_signal(ev, equity, closeadj):
    n = _mean(ev, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ev) / std(assets)
def evd_f76_ev_rnd_volratio_assets_252d_base_v067_signal(ev, assets):
    n = _std(ev, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ev) / std(assets)
def evd_f76_ev_rnd_volratio_assets_504d_base_v068_signal(ev, assets):
    n = _std(ev, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ev) / std(marketcap)
def evd_f76_ev_rnd_volratio_marketcap_252d_base_v069_signal(ev, marketcap):
    n = _std(ev, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ev) / std(marketcap)
def evd_f76_ev_rnd_volratio_marketcap_504d_base_v070_signal(ev, marketcap):
    n = _std(ev, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed ev times closeadj
def evd_f76_ev_rnd_raw_5d_base_v071_signal(ev, closeadj):
    result = _mean(ev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed ev times closeadj
def evd_f76_ev_rnd_raw_1008d_base_v072_signal(ev, closeadj):
    result = _mean(ev, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ev/assets
def evd_f76_ev_rnd_log_per_assets_252d_base_v073_signal(ev, assets):
    s = _ev_rnd_scaled(ev, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ev/assets
def evd_f76_ev_rnd_log_per_assets_504d_base_v074_signal(ev, assets):
    s = _ev_rnd_scaled(ev, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ev/marketcap
def evd_f76_ev_rnd_log_per_marketcap_252d_base_v075_signal(ev, marketcap):
    s = _ev_rnd_scaled(ev, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
