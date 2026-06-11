"""Family f086 - Daily market value and adjusted price context (Market Context from Sharadar Daily) | Sharadar tables: DAILY | fields: date, ticker, marketcap, ev, price, pb, pe, ps | base 001-075"""
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
def _daily_market_metrics_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _daily_market_metrics_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _daily_market_metrics_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed marketcap times closeadj
def dmm_f086_daily_market_metrics_raw_21d_base_v001_signal(marketcap, closeadj):
    result = _mean(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed marketcap times closeadj
def dmm_f086_daily_market_metrics_raw_63d_base_v002_signal(marketcap, closeadj):
    result = _mean(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed marketcap times closeadj
def dmm_f086_daily_market_metrics_raw_126d_base_v003_signal(marketcap, closeadj):
    result = _mean(marketcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed marketcap times closeadj
def dmm_f086_daily_market_metrics_raw_252d_base_v004_signal(marketcap, closeadj):
    result = _mean(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed marketcap times closeadj
def dmm_f086_daily_market_metrics_raw_504d_base_v005_signal(marketcap, closeadj):
    result = _mean(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(marketcap) times closeadj
def dmm_f086_daily_market_metrics_log_21d_base_v006_signal(marketcap, closeadj):
    result = _mean(_daily_market_metrics_log(marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(marketcap) times closeadj
def dmm_f086_daily_market_metrics_log_63d_base_v007_signal(marketcap, closeadj):
    result = _mean(_daily_market_metrics_log(marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(marketcap) times closeadj
def dmm_f086_daily_market_metrics_log_126d_base_v008_signal(marketcap, closeadj):
    result = _mean(_daily_market_metrics_log(marketcap), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(marketcap) times closeadj
def dmm_f086_daily_market_metrics_log_252d_base_v009_signal(marketcap, closeadj):
    result = _mean(_daily_market_metrics_log(marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(marketcap) times closeadj
def dmm_f086_daily_market_metrics_log_504d_base_v010_signal(marketcap, closeadj):
    result = _mean(_daily_market_metrics_log(marketcap), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/ev mean
def dmm_f086_daily_market_metrics_per_ev_63d_base_v011_signal(marketcap, ev):
    result = _mean(_daily_market_metrics_scaled(marketcap, ev), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/ev mean
def dmm_f086_daily_market_metrics_per_ev_252d_base_v012_signal(marketcap, ev):
    result = _mean(_daily_market_metrics_scaled(marketcap, ev), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/ev mean
def dmm_f086_daily_market_metrics_per_ev_504d_base_v013_signal(marketcap, ev):
    result = _mean(_daily_market_metrics_scaled(marketcap, ev), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/price mean
def dmm_f086_daily_market_metrics_per_price_63d_base_v014_signal(marketcap, price):
    result = _mean(_daily_market_metrics_scaled(marketcap, price), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/price mean
def dmm_f086_daily_market_metrics_per_price_252d_base_v015_signal(marketcap, price):
    result = _mean(_daily_market_metrics_scaled(marketcap, price), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/price mean
def dmm_f086_daily_market_metrics_per_price_504d_base_v016_signal(marketcap, price):
    result = _mean(_daily_market_metrics_scaled(marketcap, price), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/pb mean
def dmm_f086_daily_market_metrics_per_pb_63d_base_v017_signal(marketcap, pb):
    result = _mean(_daily_market_metrics_scaled(marketcap, pb), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/pb mean
def dmm_f086_daily_market_metrics_per_pb_252d_base_v018_signal(marketcap, pb):
    result = _mean(_daily_market_metrics_scaled(marketcap, pb), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/pb mean
def dmm_f086_daily_market_metrics_per_pb_504d_base_v019_signal(marketcap, pb):
    result = _mean(_daily_market_metrics_scaled(marketcap, pb), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/pe mean
def dmm_f086_daily_market_metrics_per_pe_63d_base_v020_signal(marketcap, pe):
    result = _mean(_daily_market_metrics_scaled(marketcap, pe), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/pe mean
def dmm_f086_daily_market_metrics_per_pe_252d_base_v021_signal(marketcap, pe):
    result = _mean(_daily_market_metrics_scaled(marketcap, pe), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/pe mean
def dmm_f086_daily_market_metrics_per_pe_504d_base_v022_signal(marketcap, pe):
    result = _mean(_daily_market_metrics_scaled(marketcap, pe), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/ps mean
def dmm_f086_daily_market_metrics_per_ps_63d_base_v023_signal(marketcap, ps):
    result = _mean(_daily_market_metrics_scaled(marketcap, ps), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/ps mean
def dmm_f086_daily_market_metrics_per_ps_252d_base_v024_signal(marketcap, ps):
    result = _mean(_daily_market_metrics_scaled(marketcap, ps), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/ps mean
def dmm_f086_daily_market_metrics_per_ps_504d_base_v025_signal(marketcap, ps):
    result = _mean(_daily_market_metrics_scaled(marketcap, ps), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap per share times closeadj
def dmm_f086_daily_market_metrics_pershare_21d_base_v026_signal(marketcap, sharesbas, closeadj):
    ps = _daily_market_metrics_per_share(marketcap, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap per share times closeadj
def dmm_f086_daily_market_metrics_pershare_63d_base_v027_signal(marketcap, sharesbas, closeadj):
    ps = _daily_market_metrics_per_share(marketcap, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d marketcap per share times closeadj
def dmm_f086_daily_market_metrics_pershare_126d_base_v028_signal(marketcap, sharesbas, closeadj):
    ps = _daily_market_metrics_per_share(marketcap, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap per share times closeadj
def dmm_f086_daily_market_metrics_pershare_252d_base_v029_signal(marketcap, sharesbas, closeadj):
    ps = _daily_market_metrics_per_share(marketcap, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap per share times closeadj
def dmm_f086_daily_market_metrics_pershare_504d_base_v030_signal(marketcap, sharesbas, closeadj):
    ps = _daily_market_metrics_per_share(marketcap, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of marketcap times closeadj
def dmm_f086_daily_market_metrics_std_63d_base_v031_signal(marketcap, closeadj):
    result = _std(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of marketcap times closeadj
def dmm_f086_daily_market_metrics_std_252d_base_v032_signal(marketcap, closeadj):
    result = _std(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of marketcap times closeadj
def dmm_f086_daily_market_metrics_std_504d_base_v033_signal(marketcap, closeadj):
    result = _std(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of marketcap
def dmm_f086_daily_market_metrics_z_252d_base_v034_signal(marketcap):
    result = _z(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of marketcap
def dmm_f086_daily_market_metrics_z_504d_base_v035_signal(marketcap):
    result = _z(marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(marketcap)
def dmm_f086_daily_market_metrics_logz_252d_base_v036_signal(marketcap):
    result = _z(_daily_market_metrics_log(marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(marketcap)
def dmm_f086_daily_market_metrics_logz_504d_base_v037_signal(marketcap):
    result = _z(_daily_market_metrics_log(marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of marketcap^2 times closeadj
def dmm_f086_daily_market_metrics_sq_63d_base_v038_signal(marketcap, closeadj):
    result = _mean(marketcap * marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of marketcap^2 times closeadj
def dmm_f086_daily_market_metrics_sq_252d_base_v039_signal(marketcap, closeadj):
    result = _mean(marketcap * marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(marketcap) times closeadj
def dmm_f086_daily_market_metrics_sign_21d_base_v040_signal(marketcap, closeadj):
    result = _mean(np.sign(marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(marketcap) times closeadj
def dmm_f086_daily_market_metrics_sign_63d_base_v041_signal(marketcap, closeadj):
    result = _mean(np.sign(marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(marketcap) times closeadj
def dmm_f086_daily_market_metrics_sign_252d_base_v042_signal(marketcap, closeadj):
    result = _mean(np.sign(marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/opex mean
def dmm_f086_daily_market_metrics_per_opex_63d_base_v043_signal(marketcap, opex):
    result = _mean(_daily_market_metrics_scaled(marketcap, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/opex mean
def dmm_f086_daily_market_metrics_per_opex_252d_base_v044_signal(marketcap, opex):
    result = _mean(_daily_market_metrics_scaled(marketcap, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/ebitda mean
def dmm_f086_daily_market_metrics_per_ebitda_63d_base_v045_signal(marketcap, ebitda):
    result = _mean(_daily_market_metrics_scaled(marketcap, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/ebitda mean
def dmm_f086_daily_market_metrics_per_ebitda_252d_base_v046_signal(marketcap, ebitda):
    result = _mean(_daily_market_metrics_scaled(marketcap, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/capex mean
def dmm_f086_daily_market_metrics_per_capex_63d_base_v047_signal(marketcap, capex):
    result = _mean(_daily_market_metrics_scaled(marketcap, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/capex mean
def dmm_f086_daily_market_metrics_per_capex_252d_base_v048_signal(marketcap, capex):
    result = _mean(_daily_market_metrics_scaled(marketcap, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/liabilities mean
def dmm_f086_daily_market_metrics_per_liabilities_63d_base_v049_signal(marketcap, liabilities):
    result = _mean(_daily_market_metrics_scaled(marketcap, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/liabilities mean
def dmm_f086_daily_market_metrics_per_liabilities_252d_base_v050_signal(marketcap, liabilities):
    result = _mean(_daily_market_metrics_scaled(marketcap, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 252d max times closeadj
def dmm_f086_daily_market_metrics_relmax_252d_base_v051_signal(marketcap, closeadj):
    peak = marketcap.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (marketcap / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 504d max times closeadj
def dmm_f086_daily_market_metrics_relmax_504d_base_v052_signal(marketcap, closeadj):
    peak = marketcap.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (marketcap / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 252d min times closeadj
def dmm_f086_daily_market_metrics_relmin_252d_base_v053_signal(marketcap, closeadj):
    trough = marketcap.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (marketcap / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 504d min times closeadj
def dmm_f086_daily_market_metrics_relmin_504d_base_v054_signal(marketcap, closeadj):
    trough = marketcap.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (marketcap / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of marketcap times closeadj
def dmm_f086_daily_market_metrics_pct_21d_base_v055_signal(marketcap, closeadj):
    result = _pct_change(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of marketcap times closeadj
def dmm_f086_daily_market_metrics_pct_63d_base_v056_signal(marketcap, closeadj):
    result = _pct_change(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of marketcap times closeadj
def dmm_f086_daily_market_metrics_pct_252d_base_v057_signal(marketcap, closeadj):
    result = _pct_change(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of marketcap times closeadj
def dmm_f086_daily_market_metrics_sum_63d_base_v058_signal(marketcap, closeadj):
    result = marketcap.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of marketcap times closeadj
def dmm_f086_daily_market_metrics_sum_252d_base_v059_signal(marketcap, closeadj):
    result = marketcap.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of marketcap times closeadj
def dmm_f086_daily_market_metrics_sum_504d_base_v060_signal(marketcap, closeadj):
    result = marketcap.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(63d) / smoothed ev(252d) x closeadj
def dmm_f086_daily_market_metrics_rom_ev_252_63d_base_v061_signal(marketcap, ev, closeadj):
    n = _mean(marketcap, 63)
    d = _mean(ev, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(126d) / smoothed ev(504d) x closeadj
def dmm_f086_daily_market_metrics_rom_ev_504_126d_base_v062_signal(marketcap, ev, closeadj):
    n = _mean(marketcap, 126)
    d = _mean(ev, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(63d) / smoothed price(252d) x closeadj
def dmm_f086_daily_market_metrics_rom_price_252_63d_base_v063_signal(marketcap, price, closeadj):
    n = _mean(marketcap, 63)
    d = _mean(price, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(126d) / smoothed price(504d) x closeadj
def dmm_f086_daily_market_metrics_rom_price_504_126d_base_v064_signal(marketcap, price, closeadj):
    n = _mean(marketcap, 126)
    d = _mean(price, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(63d) / smoothed pb(252d) x closeadj
def dmm_f086_daily_market_metrics_rom_pb_252_63d_base_v065_signal(marketcap, pb, closeadj):
    n = _mean(marketcap, 63)
    d = _mean(pb, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(126d) / smoothed pb(504d) x closeadj
def dmm_f086_daily_market_metrics_rom_pb_504_126d_base_v066_signal(marketcap, pb, closeadj):
    n = _mean(marketcap, 126)
    d = _mean(pb, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(marketcap) / std(ev)
def dmm_f086_daily_market_metrics_volratio_ev_252d_base_v067_signal(marketcap, ev):
    n = _std(marketcap, 252)
    d = _std(ev, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(marketcap) / std(ev)
def dmm_f086_daily_market_metrics_volratio_ev_504d_base_v068_signal(marketcap, ev):
    n = _std(marketcap, 504)
    d = _std(ev, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(marketcap) / std(price)
def dmm_f086_daily_market_metrics_volratio_price_252d_base_v069_signal(marketcap, price):
    n = _std(marketcap, 252)
    d = _std(price, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(marketcap) / std(price)
def dmm_f086_daily_market_metrics_volratio_price_504d_base_v070_signal(marketcap, price):
    n = _std(marketcap, 504)
    d = _std(price, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed marketcap times closeadj
def dmm_f086_daily_market_metrics_raw_5d_base_v071_signal(marketcap, closeadj):
    result = _mean(marketcap, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed marketcap times closeadj
def dmm_f086_daily_market_metrics_raw_1008d_base_v072_signal(marketcap, closeadj):
    result = _mean(marketcap, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of marketcap/ev
def dmm_f086_daily_market_metrics_log_per_ev_252d_base_v073_signal(marketcap, ev):
    s = _daily_market_metrics_scaled(marketcap, ev)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of marketcap/ev
def dmm_f086_daily_market_metrics_log_per_ev_504d_base_v074_signal(marketcap, ev):
    s = _daily_market_metrics_scaled(marketcap, ev)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of marketcap/price
def dmm_f086_daily_market_metrics_log_per_price_252d_base_v075_signal(marketcap, price):
    s = _daily_market_metrics_scaled(marketcap, price)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
