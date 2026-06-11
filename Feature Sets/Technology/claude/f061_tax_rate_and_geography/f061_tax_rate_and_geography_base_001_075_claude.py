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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f061_eff_tax(taxexp, ebt):
    return taxexp / ebt.replace(0, np.nan).abs()


# 21d mean of eff_tax_rate scaled by closeadj
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_mean_21d_base_v001_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eff_tax_rate scaled by closeadj
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_mean_63d_base_v002_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eff_tax_rate scaled by closeadj
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_mean_126d_base_v003_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eff_tax_rate scaled by closeadj
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_mean_252d_base_v004_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eff_tax_rate scaled by closeadj
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_mean_504d_base_v005_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tax_vol_252 scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_vol_252_mean_21d_base_v006_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tax_vol_252 scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_vol_252_mean_63d_base_v007_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tax_vol_252 scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_vol_252_mean_126d_base_v008_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tax_vol_252 scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_vol_252_mean_252d_base_v009_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tax_vol_252 scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_vol_252_mean_504d_base_v010_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tax_assets_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_assets_share_mean_21d_base_v011_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tax_assets_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_assets_share_mean_63d_base_v012_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tax_assets_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_assets_share_mean_126d_base_v013_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tax_assets_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_assets_share_mean_252d_base_v014_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tax_assets_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_assets_share_mean_504d_base_v015_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tax_liab_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_liab_share_mean_21d_base_v016_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tax_liab_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_liab_share_mean_63d_base_v017_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tax_liab_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_liab_share_mean_126d_base_v018_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tax_liab_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_liab_share_mean_252d_base_v019_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tax_liab_share scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_liab_share_mean_504d_base_v020_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of net_tax_pos scaled by closeadj
def f061trx_f061_tax_rate_and_geography_net_tax_pos_mean_21d_base_v021_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of net_tax_pos scaled by closeadj
def f061trx_f061_tax_rate_and_geography_net_tax_pos_mean_63d_base_v022_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of net_tax_pos scaled by closeadj
def f061trx_f061_tax_rate_and_geography_net_tax_pos_mean_126d_base_v023_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of net_tax_pos scaled by closeadj
def f061trx_f061_tax_rate_and_geography_net_tax_pos_mean_252d_base_v024_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of net_tax_pos scaled by closeadj
def f061trx_f061_tax_rate_and_geography_net_tax_pos_mean_504d_base_v025_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tax_to_rev scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_to_rev_mean_21d_base_v026_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tax_to_rev scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_to_rev_mean_63d_base_v027_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tax_to_rev scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_to_rev_mean_126d_base_v028_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tax_to_rev scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_to_rev_mean_252d_base_v029_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tax_to_rev scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_to_rev_mean_504d_base_v030_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tax_yoy_chg scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_mean_21d_base_v031_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tax_yoy_chg scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_mean_63d_base_v032_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tax_yoy_chg scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_mean_126d_base_v033_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tax_yoy_chg scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_mean_252d_base_v034_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tax_yoy_chg scaled by closeadj
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_mean_504d_base_v035_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_median_63d_base_v036_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_median_252d_base_v037_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_median_504d_base_v038_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_median_63d_base_v039_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_median_252d_base_v040_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_median_504d_base_v041_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_median_63d_base_v042_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_median_252d_base_v043_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_median_504d_base_v044_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_median_63d_base_v045_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_median_252d_base_v046_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_median_504d_base_v047_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_median_63d_base_v048_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_median_252d_base_v049_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_median_504d_base_v050_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_median_63d_base_v051_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_median_252d_base_v052_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_median_504d_base_v053_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_median_63d_base_v054_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_median_252d_base_v055_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_median_504d_base_v056_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_rmax_252d_base_v057_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_rmax_504d_base_v058_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_rmax_252d_base_v059_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_rmax_504d_base_v060_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_rmax_252d_base_v061_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_rmax_504d_base_v062_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_rmax_252d_base_v063_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_rmax_504d_base_v064_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_rmax_252d_base_v065_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_rmax_504d_base_v066_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_rmax_252d_base_v067_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_rmax_504d_base_v068_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_rmax_252d_base_v069_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_rmax_504d_base_v070_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_rmin_252d_base_v071_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_rmin_504d_base_v072_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_rmin_252d_base_v073_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_rmin_504d_base_v074_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_rmin_252d_base_v075_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

