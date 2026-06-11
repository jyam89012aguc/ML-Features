"""Family f071 - Book and tangible book valuation (Valuation Multiples) | Sharadar tables: DAILY,SF1 | fields: pb, bvps, tbvps, marketcap, equity | base 001-075"""
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
def _price_book_valuation_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _price_book_valuation_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _price_book_valuation_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed pb times closeadj
def pbv_f071_price_book_valuation_raw_21d_base_v001_signal(pb, closeadj):
    result = _mean(pb, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed pb times closeadj
def pbv_f071_price_book_valuation_raw_63d_base_v002_signal(pb, closeadj):
    result = _mean(pb, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed pb times closeadj
def pbv_f071_price_book_valuation_raw_126d_base_v003_signal(pb, closeadj):
    result = _mean(pb, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed pb times closeadj
def pbv_f071_price_book_valuation_raw_252d_base_v004_signal(pb, closeadj):
    result = _mean(pb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed pb times closeadj
def pbv_f071_price_book_valuation_raw_504d_base_v005_signal(pb, closeadj):
    result = _mean(pb, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(pb) times closeadj
def pbv_f071_price_book_valuation_log_21d_base_v006_signal(pb, closeadj):
    result = _mean(_price_book_valuation_log(pb), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(pb) times closeadj
def pbv_f071_price_book_valuation_log_63d_base_v007_signal(pb, closeadj):
    result = _mean(_price_book_valuation_log(pb), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(pb) times closeadj
def pbv_f071_price_book_valuation_log_126d_base_v008_signal(pb, closeadj):
    result = _mean(_price_book_valuation_log(pb), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(pb) times closeadj
def pbv_f071_price_book_valuation_log_252d_base_v009_signal(pb, closeadj):
    result = _mean(_price_book_valuation_log(pb), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(pb) times closeadj
def pbv_f071_price_book_valuation_log_504d_base_v010_signal(pb, closeadj):
    result = _mean(_price_book_valuation_log(pb), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb/bvps mean
def pbv_f071_price_book_valuation_per_bvps_63d_base_v011_signal(pb, bvps):
    result = _mean(_price_book_valuation_scaled(pb, bvps), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb/bvps mean
def pbv_f071_price_book_valuation_per_bvps_252d_base_v012_signal(pb, bvps):
    result = _mean(_price_book_valuation_scaled(pb, bvps), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pb/bvps mean
def pbv_f071_price_book_valuation_per_bvps_504d_base_v013_signal(pb, bvps):
    result = _mean(_price_book_valuation_scaled(pb, bvps), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb/tbvps mean
def pbv_f071_price_book_valuation_per_tbvps_63d_base_v014_signal(pb, tbvps):
    result = _mean(_price_book_valuation_scaled(pb, tbvps), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb/tbvps mean
def pbv_f071_price_book_valuation_per_tbvps_252d_base_v015_signal(pb, tbvps):
    result = _mean(_price_book_valuation_scaled(pb, tbvps), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pb/tbvps mean
def pbv_f071_price_book_valuation_per_tbvps_504d_base_v016_signal(pb, tbvps):
    result = _mean(_price_book_valuation_scaled(pb, tbvps), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb/marketcap mean
def pbv_f071_price_book_valuation_per_marketcap_63d_base_v017_signal(pb, marketcap):
    result = _mean(_price_book_valuation_scaled(pb, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb/marketcap mean
def pbv_f071_price_book_valuation_per_marketcap_252d_base_v018_signal(pb, marketcap):
    result = _mean(_price_book_valuation_scaled(pb, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pb/marketcap mean
def pbv_f071_price_book_valuation_per_marketcap_504d_base_v019_signal(pb, marketcap):
    result = _mean(_price_book_valuation_scaled(pb, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb/equity mean
def pbv_f071_price_book_valuation_per_equity_63d_base_v020_signal(pb, equity):
    result = _mean(_price_book_valuation_scaled(pb, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb/equity mean
def pbv_f071_price_book_valuation_per_equity_252d_base_v021_signal(pb, equity):
    result = _mean(_price_book_valuation_scaled(pb, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pb/equity mean
def pbv_f071_price_book_valuation_per_equity_504d_base_v022_signal(pb, equity):
    result = _mean(_price_book_valuation_scaled(pb, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb/assets mean
def pbv_f071_price_book_valuation_per_assets_63d_base_v023_signal(pb, assets):
    result = _mean(_price_book_valuation_scaled(pb, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb/assets mean
def pbv_f071_price_book_valuation_per_assets_252d_base_v024_signal(pb, assets):
    result = _mean(_price_book_valuation_scaled(pb, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pb/assets mean
def pbv_f071_price_book_valuation_per_assets_504d_base_v025_signal(pb, assets):
    result = _mean(_price_book_valuation_scaled(pb, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pb per share times closeadj
def pbv_f071_price_book_valuation_pershare_21d_base_v026_signal(pb, sharesbas, closeadj):
    ps = _price_book_valuation_per_share(pb, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb per share times closeadj
def pbv_f071_price_book_valuation_pershare_63d_base_v027_signal(pb, sharesbas, closeadj):
    ps = _price_book_valuation_per_share(pb, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pb per share times closeadj
def pbv_f071_price_book_valuation_pershare_126d_base_v028_signal(pb, sharesbas, closeadj):
    ps = _price_book_valuation_per_share(pb, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb per share times closeadj
def pbv_f071_price_book_valuation_pershare_252d_base_v029_signal(pb, sharesbas, closeadj):
    ps = _price_book_valuation_per_share(pb, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pb per share times closeadj
def pbv_f071_price_book_valuation_pershare_504d_base_v030_signal(pb, sharesbas, closeadj):
    ps = _price_book_valuation_per_share(pb, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of pb times closeadj
def pbv_f071_price_book_valuation_std_63d_base_v031_signal(pb, closeadj):
    result = _std(pb, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of pb times closeadj
def pbv_f071_price_book_valuation_std_252d_base_v032_signal(pb, closeadj):
    result = _std(pb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of pb times closeadj
def pbv_f071_price_book_valuation_std_504d_base_v033_signal(pb, closeadj):
    result = _std(pb, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of pb
def pbv_f071_price_book_valuation_z_252d_base_v034_signal(pb):
    result = _z(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of pb
def pbv_f071_price_book_valuation_z_504d_base_v035_signal(pb):
    result = _z(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(pb)
def pbv_f071_price_book_valuation_logz_252d_base_v036_signal(pb):
    result = _z(_price_book_valuation_log(pb), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(pb)
def pbv_f071_price_book_valuation_logz_504d_base_v037_signal(pb):
    result = _z(_price_book_valuation_log(pb), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of pb^2 times closeadj
def pbv_f071_price_book_valuation_sq_63d_base_v038_signal(pb, closeadj):
    result = _mean(pb * pb, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of pb^2 times closeadj
def pbv_f071_price_book_valuation_sq_252d_base_v039_signal(pb, closeadj):
    result = _mean(pb * pb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(pb) times closeadj
def pbv_f071_price_book_valuation_sign_21d_base_v040_signal(pb, closeadj):
    result = _mean(np.sign(pb), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(pb) times closeadj
def pbv_f071_price_book_valuation_sign_63d_base_v041_signal(pb, closeadj):
    result = _mean(np.sign(pb), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(pb) times closeadj
def pbv_f071_price_book_valuation_sign_252d_base_v042_signal(pb, closeadj):
    result = _mean(np.sign(pb), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb/opex mean
def pbv_f071_price_book_valuation_per_opex_63d_base_v043_signal(pb, opex):
    result = _mean(_price_book_valuation_scaled(pb, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb/opex mean
def pbv_f071_price_book_valuation_per_opex_252d_base_v044_signal(pb, opex):
    result = _mean(_price_book_valuation_scaled(pb, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb/ebitda mean
def pbv_f071_price_book_valuation_per_ebitda_63d_base_v045_signal(pb, ebitda):
    result = _mean(_price_book_valuation_scaled(pb, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb/ebitda mean
def pbv_f071_price_book_valuation_per_ebitda_252d_base_v046_signal(pb, ebitda):
    result = _mean(_price_book_valuation_scaled(pb, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb/capex mean
def pbv_f071_price_book_valuation_per_capex_63d_base_v047_signal(pb, capex):
    result = _mean(_price_book_valuation_scaled(pb, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb/capex mean
def pbv_f071_price_book_valuation_per_capex_252d_base_v048_signal(pb, capex):
    result = _mean(_price_book_valuation_scaled(pb, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pb/liabilities mean
def pbv_f071_price_book_valuation_per_liabilities_63d_base_v049_signal(pb, liabilities):
    result = _mean(_price_book_valuation_scaled(pb, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb/liabilities mean
def pbv_f071_price_book_valuation_per_liabilities_252d_base_v050_signal(pb, liabilities):
    result = _mean(_price_book_valuation_scaled(pb, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pb relative to 252d max times closeadj
def pbv_f071_price_book_valuation_relmax_252d_base_v051_signal(pb, closeadj):
    peak = pb.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (pb / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pb relative to 504d max times closeadj
def pbv_f071_price_book_valuation_relmax_504d_base_v052_signal(pb, closeadj):
    peak = pb.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (pb / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pb relative to 252d min times closeadj
def pbv_f071_price_book_valuation_relmin_252d_base_v053_signal(pb, closeadj):
    trough = pb.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (pb / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pb relative to 504d min times closeadj
def pbv_f071_price_book_valuation_relmin_504d_base_v054_signal(pb, closeadj):
    trough = pb.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (pb / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of pb times closeadj
def pbv_f071_price_book_valuation_pct_21d_base_v055_signal(pb, closeadj):
    result = _pct_change(pb, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of pb times closeadj
def pbv_f071_price_book_valuation_pct_63d_base_v056_signal(pb, closeadj):
    result = _pct_change(pb, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of pb times closeadj
def pbv_f071_price_book_valuation_pct_252d_base_v057_signal(pb, closeadj):
    result = _pct_change(pb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of pb times closeadj
def pbv_f071_price_book_valuation_sum_63d_base_v058_signal(pb, closeadj):
    result = pb.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of pb times closeadj
def pbv_f071_price_book_valuation_sum_252d_base_v059_signal(pb, closeadj):
    result = pb.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of pb times closeadj
def pbv_f071_price_book_valuation_sum_504d_base_v060_signal(pb, closeadj):
    result = pb.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pb(63d) / smoothed bvps(252d) x closeadj
def pbv_f071_price_book_valuation_rom_bvps_252_63d_base_v061_signal(pb, bvps, closeadj):
    n = _mean(pb, 63)
    d = _mean(bvps, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pb(126d) / smoothed bvps(504d) x closeadj
def pbv_f071_price_book_valuation_rom_bvps_504_126d_base_v062_signal(pb, bvps, closeadj):
    n = _mean(pb, 126)
    d = _mean(bvps, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pb(63d) / smoothed tbvps(252d) x closeadj
def pbv_f071_price_book_valuation_rom_tbvps_252_63d_base_v063_signal(pb, tbvps, closeadj):
    n = _mean(pb, 63)
    d = _mean(tbvps, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pb(126d) / smoothed tbvps(504d) x closeadj
def pbv_f071_price_book_valuation_rom_tbvps_504_126d_base_v064_signal(pb, tbvps, closeadj):
    n = _mean(pb, 126)
    d = _mean(tbvps, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pb(63d) / smoothed marketcap(252d) x closeadj
def pbv_f071_price_book_valuation_rom_marketcap_252_63d_base_v065_signal(pb, marketcap, closeadj):
    n = _mean(pb, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed pb(126d) / smoothed marketcap(504d) x closeadj
def pbv_f071_price_book_valuation_rom_marketcap_504_126d_base_v066_signal(pb, marketcap, closeadj):
    n = _mean(pb, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(pb) / std(bvps)
def pbv_f071_price_book_valuation_volratio_bvps_252d_base_v067_signal(pb, bvps):
    n = _std(pb, 252)
    d = _std(bvps, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(pb) / std(bvps)
def pbv_f071_price_book_valuation_volratio_bvps_504d_base_v068_signal(pb, bvps):
    n = _std(pb, 504)
    d = _std(bvps, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(pb) / std(tbvps)
def pbv_f071_price_book_valuation_volratio_tbvps_252d_base_v069_signal(pb, tbvps):
    n = _std(pb, 252)
    d = _std(tbvps, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(pb) / std(tbvps)
def pbv_f071_price_book_valuation_volratio_tbvps_504d_base_v070_signal(pb, tbvps):
    n = _std(pb, 504)
    d = _std(tbvps, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed pb times closeadj
def pbv_f071_price_book_valuation_raw_5d_base_v071_signal(pb, closeadj):
    result = _mean(pb, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed pb times closeadj
def pbv_f071_price_book_valuation_raw_1008d_base_v072_signal(pb, closeadj):
    result = _mean(pb, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of pb/bvps
def pbv_f071_price_book_valuation_log_per_bvps_252d_base_v073_signal(pb, bvps):
    s = _price_book_valuation_scaled(pb, bvps)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of pb/bvps
def pbv_f071_price_book_valuation_log_per_bvps_504d_base_v074_signal(pb, bvps):
    s = _price_book_valuation_scaled(pb, bvps)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of pb/tbvps
def pbv_f071_price_book_valuation_log_per_tbvps_252d_base_v075_signal(pb, tbvps):
    s = _price_book_valuation_scaled(pb, tbvps)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
