"""Family f020 - SG&A versus R&D mix (R&D and Innovation) | Sharadar tables: SF1 | fields: sgna, rnd, opex | base 001-075"""
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
def _sga_rnd_mix_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sga_rnd_mix_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sga_rnd_mix_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed sgna times closeadj
def srm_f020_sga_rnd_mix_raw_21d_base_v001_signal(sgna, closeadj):
    result = _mean(sgna, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed sgna times closeadj
def srm_f020_sga_rnd_mix_raw_63d_base_v002_signal(sgna, closeadj):
    result = _mean(sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed sgna times closeadj
def srm_f020_sga_rnd_mix_raw_126d_base_v003_signal(sgna, closeadj):
    result = _mean(sgna, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed sgna times closeadj
def srm_f020_sga_rnd_mix_raw_252d_base_v004_signal(sgna, closeadj):
    result = _mean(sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed sgna times closeadj
def srm_f020_sga_rnd_mix_raw_504d_base_v005_signal(sgna, closeadj):
    result = _mean(sgna, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(sgna) times closeadj
def srm_f020_sga_rnd_mix_log_21d_base_v006_signal(sgna, closeadj):
    result = _mean(_sga_rnd_mix_log(sgna), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(sgna) times closeadj
def srm_f020_sga_rnd_mix_log_63d_base_v007_signal(sgna, closeadj):
    result = _mean(_sga_rnd_mix_log(sgna), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(sgna) times closeadj
def srm_f020_sga_rnd_mix_log_126d_base_v008_signal(sgna, closeadj):
    result = _mean(_sga_rnd_mix_log(sgna), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(sgna) times closeadj
def srm_f020_sga_rnd_mix_log_252d_base_v009_signal(sgna, closeadj):
    result = _mean(_sga_rnd_mix_log(sgna), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(sgna) times closeadj
def srm_f020_sga_rnd_mix_log_504d_base_v010_signal(sgna, closeadj):
    result = _mean(_sga_rnd_mix_log(sgna), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/rnd mean
def srm_f020_sga_rnd_mix_per_rnd_63d_base_v011_signal(sgna, rnd):
    result = _mean(_sga_rnd_mix_scaled(sgna, rnd), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/rnd mean
def srm_f020_sga_rnd_mix_per_rnd_252d_base_v012_signal(sgna, rnd):
    result = _mean(_sga_rnd_mix_scaled(sgna, rnd), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/rnd mean
def srm_f020_sga_rnd_mix_per_rnd_504d_base_v013_signal(sgna, rnd):
    result = _mean(_sga_rnd_mix_scaled(sgna, rnd), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/assets mean
def srm_f020_sga_rnd_mix_per_assets_63d_base_v014_signal(sgna, assets):
    result = _mean(_sga_rnd_mix_scaled(sgna, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/assets mean
def srm_f020_sga_rnd_mix_per_assets_252d_base_v015_signal(sgna, assets):
    result = _mean(_sga_rnd_mix_scaled(sgna, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/assets mean
def srm_f020_sga_rnd_mix_per_assets_504d_base_v016_signal(sgna, assets):
    result = _mean(_sga_rnd_mix_scaled(sgna, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/marketcap mean
def srm_f020_sga_rnd_mix_per_marketcap_63d_base_v017_signal(sgna, marketcap):
    result = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/marketcap mean
def srm_f020_sga_rnd_mix_per_marketcap_252d_base_v018_signal(sgna, marketcap):
    result = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/marketcap mean
def srm_f020_sga_rnd_mix_per_marketcap_504d_base_v019_signal(sgna, marketcap):
    result = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/equity mean
def srm_f020_sga_rnd_mix_per_equity_63d_base_v020_signal(sgna, equity):
    result = _mean(_sga_rnd_mix_scaled(sgna, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/equity mean
def srm_f020_sga_rnd_mix_per_equity_252d_base_v021_signal(sgna, equity):
    result = _mean(_sga_rnd_mix_scaled(sgna, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/equity mean
def srm_f020_sga_rnd_mix_per_equity_504d_base_v022_signal(sgna, equity):
    result = _mean(_sga_rnd_mix_scaled(sgna, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/debt mean
def srm_f020_sga_rnd_mix_per_debt_63d_base_v023_signal(sgna, debt):
    result = _mean(_sga_rnd_mix_scaled(sgna, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/debt mean
def srm_f020_sga_rnd_mix_per_debt_252d_base_v024_signal(sgna, debt):
    result = _mean(_sga_rnd_mix_scaled(sgna, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna/debt mean
def srm_f020_sga_rnd_mix_per_debt_504d_base_v025_signal(sgna, debt):
    result = _mean(_sga_rnd_mix_scaled(sgna, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sgna per share times closeadj
def srm_f020_sga_rnd_mix_pershare_21d_base_v026_signal(sgna, sharesbas, closeadj):
    ps = _sga_rnd_mix_per_share(sgna, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna per share times closeadj
def srm_f020_sga_rnd_mix_pershare_63d_base_v027_signal(sgna, sharesbas, closeadj):
    ps = _sga_rnd_mix_per_share(sgna, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sgna per share times closeadj
def srm_f020_sga_rnd_mix_pershare_126d_base_v028_signal(sgna, sharesbas, closeadj):
    ps = _sga_rnd_mix_per_share(sgna, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna per share times closeadj
def srm_f020_sga_rnd_mix_pershare_252d_base_v029_signal(sgna, sharesbas, closeadj):
    ps = _sga_rnd_mix_per_share(sgna, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sgna per share times closeadj
def srm_f020_sga_rnd_mix_pershare_504d_base_v030_signal(sgna, sharesbas, closeadj):
    ps = _sga_rnd_mix_per_share(sgna, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of sgna times closeadj
def srm_f020_sga_rnd_mix_std_63d_base_v031_signal(sgna, closeadj):
    result = _std(sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of sgna times closeadj
def srm_f020_sga_rnd_mix_std_252d_base_v032_signal(sgna, closeadj):
    result = _std(sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of sgna times closeadj
def srm_f020_sga_rnd_mix_std_504d_base_v033_signal(sgna, closeadj):
    result = _std(sgna, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of sgna
def srm_f020_sga_rnd_mix_z_252d_base_v034_signal(sgna):
    result = _z(sgna, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of sgna
def srm_f020_sga_rnd_mix_z_504d_base_v035_signal(sgna):
    result = _z(sgna, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(sgna)
def srm_f020_sga_rnd_mix_logz_252d_base_v036_signal(sgna):
    result = _z(_sga_rnd_mix_log(sgna), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(sgna)
def srm_f020_sga_rnd_mix_logz_504d_base_v037_signal(sgna):
    result = _z(_sga_rnd_mix_log(sgna), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sgna^2 times closeadj
def srm_f020_sga_rnd_mix_sq_63d_base_v038_signal(sgna, closeadj):
    result = _mean(sgna * sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sgna^2 times closeadj
def srm_f020_sga_rnd_mix_sq_252d_base_v039_signal(sgna, closeadj):
    result = _mean(sgna * sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(sgna) times closeadj
def srm_f020_sga_rnd_mix_sign_21d_base_v040_signal(sgna, closeadj):
    result = _mean(np.sign(sgna), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(sgna) times closeadj
def srm_f020_sga_rnd_mix_sign_63d_base_v041_signal(sgna, closeadj):
    result = _mean(np.sign(sgna), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(sgna) times closeadj
def srm_f020_sga_rnd_mix_sign_252d_base_v042_signal(sgna, closeadj):
    result = _mean(np.sign(sgna), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/opex mean
def srm_f020_sga_rnd_mix_per_opex_63d_base_v043_signal(sgna, opex):
    result = _mean(_sga_rnd_mix_scaled(sgna, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/opex mean
def srm_f020_sga_rnd_mix_per_opex_252d_base_v044_signal(sgna, opex):
    result = _mean(_sga_rnd_mix_scaled(sgna, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/ebitda mean
def srm_f020_sga_rnd_mix_per_ebitda_63d_base_v045_signal(sgna, ebitda):
    result = _mean(_sga_rnd_mix_scaled(sgna, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/ebitda mean
def srm_f020_sga_rnd_mix_per_ebitda_252d_base_v046_signal(sgna, ebitda):
    result = _mean(_sga_rnd_mix_scaled(sgna, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/capex mean
def srm_f020_sga_rnd_mix_per_capex_63d_base_v047_signal(sgna, capex):
    result = _mean(_sga_rnd_mix_scaled(sgna, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/capex mean
def srm_f020_sga_rnd_mix_per_capex_252d_base_v048_signal(sgna, capex):
    result = _mean(_sga_rnd_mix_scaled(sgna, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sgna/liabilities mean
def srm_f020_sga_rnd_mix_per_liabilities_63d_base_v049_signal(sgna, liabilities):
    result = _mean(_sga_rnd_mix_scaled(sgna, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sgna/liabilities mean
def srm_f020_sga_rnd_mix_per_liabilities_252d_base_v050_signal(sgna, liabilities):
    result = _mean(_sga_rnd_mix_scaled(sgna, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 252d max times closeadj
def srm_f020_sga_rnd_mix_relmax_252d_base_v051_signal(sgna, closeadj):
    peak = sgna.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (sgna / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 504d max times closeadj
def srm_f020_sga_rnd_mix_relmax_504d_base_v052_signal(sgna, closeadj):
    peak = sgna.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (sgna / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 252d min times closeadj
def srm_f020_sga_rnd_mix_relmin_252d_base_v053_signal(sgna, closeadj):
    trough = sgna.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (sgna / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 504d min times closeadj
def srm_f020_sga_rnd_mix_relmin_504d_base_v054_signal(sgna, closeadj):
    trough = sgna.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (sgna / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of sgna times closeadj
def srm_f020_sga_rnd_mix_pct_21d_base_v055_signal(sgna, closeadj):
    result = _pct_change(sgna, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of sgna times closeadj
def srm_f020_sga_rnd_mix_pct_63d_base_v056_signal(sgna, closeadj):
    result = _pct_change(sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of sgna times closeadj
def srm_f020_sga_rnd_mix_pct_252d_base_v057_signal(sgna, closeadj):
    result = _pct_change(sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of sgna times closeadj
def srm_f020_sga_rnd_mix_sum_63d_base_v058_signal(sgna, closeadj):
    result = sgna.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of sgna times closeadj
def srm_f020_sga_rnd_mix_sum_252d_base_v059_signal(sgna, closeadj):
    result = sgna.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of sgna times closeadj
def srm_f020_sga_rnd_mix_sum_504d_base_v060_signal(sgna, closeadj):
    result = sgna.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(63d) / smoothed rnd(252d) x closeadj
def srm_f020_sga_rnd_mix_rom_rnd_252_63d_base_v061_signal(sgna, rnd, closeadj):
    n = _mean(sgna, 63)
    d = _mean(rnd, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(126d) / smoothed rnd(504d) x closeadj
def srm_f020_sga_rnd_mix_rom_rnd_504_126d_base_v062_signal(sgna, rnd, closeadj):
    n = _mean(sgna, 126)
    d = _mean(rnd, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(63d) / smoothed assets(252d) x closeadj
def srm_f020_sga_rnd_mix_rom_assets_252_63d_base_v063_signal(sgna, assets, closeadj):
    n = _mean(sgna, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(126d) / smoothed assets(504d) x closeadj
def srm_f020_sga_rnd_mix_rom_assets_504_126d_base_v064_signal(sgna, assets, closeadj):
    n = _mean(sgna, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(63d) / smoothed marketcap(252d) x closeadj
def srm_f020_sga_rnd_mix_rom_marketcap_252_63d_base_v065_signal(sgna, marketcap, closeadj):
    n = _mean(sgna, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sgna(126d) / smoothed marketcap(504d) x closeadj
def srm_f020_sga_rnd_mix_rom_marketcap_504_126d_base_v066_signal(sgna, marketcap, closeadj):
    n = _mean(sgna, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sgna) / std(rnd)
def srm_f020_sga_rnd_mix_volratio_rnd_252d_base_v067_signal(sgna, rnd):
    n = _std(sgna, 252)
    d = _std(rnd, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sgna) / std(rnd)
def srm_f020_sga_rnd_mix_volratio_rnd_504d_base_v068_signal(sgna, rnd):
    n = _std(sgna, 504)
    d = _std(rnd, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sgna) / std(assets)
def srm_f020_sga_rnd_mix_volratio_assets_252d_base_v069_signal(sgna, assets):
    n = _std(sgna, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sgna) / std(assets)
def srm_f020_sga_rnd_mix_volratio_assets_504d_base_v070_signal(sgna, assets):
    n = _std(sgna, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed sgna times closeadj
def srm_f020_sga_rnd_mix_raw_5d_base_v071_signal(sgna, closeadj):
    result = _mean(sgna, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed sgna times closeadj
def srm_f020_sga_rnd_mix_raw_1008d_base_v072_signal(sgna, closeadj):
    result = _mean(sgna, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sgna/rnd
def srm_f020_sga_rnd_mix_log_per_rnd_252d_base_v073_signal(sgna, rnd):
    s = _sga_rnd_mix_scaled(sgna, rnd)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sgna/rnd
def srm_f020_sga_rnd_mix_log_per_rnd_504d_base_v074_signal(sgna, rnd):
    s = _sga_rnd_mix_scaled(sgna, rnd)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sgna/assets
def srm_f020_sga_rnd_mix_log_per_assets_252d_base_v075_signal(sgna, assets):
    s = _sga_rnd_mix_scaled(sgna, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
