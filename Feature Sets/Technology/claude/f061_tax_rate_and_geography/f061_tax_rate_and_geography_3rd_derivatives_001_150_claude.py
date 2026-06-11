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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f061_eff_tax(taxexp, ebt):
    return taxexp / ebt.replace(0, np.nan).abs()


# 21d acceleration of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_accel_21d_3d_v001_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_accel_63d_3d_v002_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_accel_126d_3d_v003_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_accel_252d_3d_v004_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_accel_21d_3d_v005_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_accel_63d_3d_v006_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_accel_126d_3d_v007_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_accel_252d_3d_v008_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_accel_21d_3d_v009_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_accel_63d_3d_v010_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_accel_126d_3d_v011_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_accel_252d_3d_v012_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_accel_21d_3d_v013_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_accel_63d_3d_v014_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_accel_126d_3d_v015_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_accel_252d_3d_v016_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_accel_21d_3d_v017_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_accel_63d_3d_v018_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_accel_126d_3d_v019_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_accel_252d_3d_v020_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_accel_21d_3d_v021_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_accel_63d_3d_v022_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_accel_126d_3d_v023_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_accel_252d_3d_v024_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_accel_21d_3d_v025_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_accel_63d_3d_v026_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_accel_126d_3d_v027_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_accel_252d_3d_v028_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_slopez_21d_z126_3d_v029_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_slopez_63d_z252_3d_v030_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_slopez_126d_z252_3d_v031_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_slopez_252d_z504_3d_v032_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_slopez_21d_z126_3d_v033_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_slopez_63d_z252_3d_v034_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_slopez_126d_z252_3d_v035_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_slopez_252d_z504_3d_v036_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_slopez_21d_z126_3d_v037_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_slopez_63d_z252_3d_v038_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_slopez_126d_z252_3d_v039_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_slopez_252d_z504_3d_v040_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_slopez_21d_z126_3d_v041_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_slopez_63d_z252_3d_v042_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_slopez_126d_z252_3d_v043_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_slopez_252d_z504_3d_v044_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_slopez_21d_z126_3d_v045_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_slopez_63d_z252_3d_v046_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_slopez_126d_z252_3d_v047_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_slopez_252d_z504_3d_v048_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_slopez_21d_z126_3d_v049_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_slopez_63d_z252_3d_v050_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_slopez_126d_z252_3d_v051_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_slopez_252d_z504_3d_v052_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_slopez_21d_z126_3d_v053_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_slopez_63d_z252_3d_v054_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_slopez_126d_z252_3d_v055_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_slopez_252d_z504_3d_v056_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_jerk_21d_3d_v057_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_jerk_63d_3d_v058_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_jerk_126d_3d_v059_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_jerk_21d_3d_v060_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_jerk_63d_3d_v061_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_jerk_126d_3d_v062_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_jerk_21d_3d_v063_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_jerk_63d_3d_v064_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_jerk_126d_3d_v065_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_jerk_21d_3d_v066_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_jerk_63d_3d_v067_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_jerk_126d_3d_v068_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_jerk_21d_3d_v069_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_jerk_63d_3d_v070_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_jerk_126d_3d_v071_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_jerk_21d_3d_v072_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_jerk_63d_3d_v073_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_jerk_126d_3d_v074_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_jerk_21d_3d_v075_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_jerk_63d_3d_v076_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_jerk_126d_3d_v077_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eff_tax_rate smoothed over 252d
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_smoothaccel_63d_sm252_3d_v078_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eff_tax_rate smoothed over 504d
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_smoothaccel_252d_sm504_3d_v079_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tax_vol_252 smoothed over 252d
def f061trx_f061_tax_rate_and_geography_tax_vol_252_smoothaccel_63d_sm252_3d_v080_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tax_vol_252 smoothed over 504d
def f061trx_f061_tax_rate_and_geography_tax_vol_252_smoothaccel_252d_sm504_3d_v081_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tax_assets_share smoothed over 252d
def f061trx_f061_tax_rate_and_geography_tax_assets_share_smoothaccel_63d_sm252_3d_v082_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tax_assets_share smoothed over 504d
def f061trx_f061_tax_rate_and_geography_tax_assets_share_smoothaccel_252d_sm504_3d_v083_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tax_liab_share smoothed over 252d
def f061trx_f061_tax_rate_and_geography_tax_liab_share_smoothaccel_63d_sm252_3d_v084_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tax_liab_share smoothed over 504d
def f061trx_f061_tax_rate_and_geography_tax_liab_share_smoothaccel_252d_sm504_3d_v085_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of net_tax_pos smoothed over 252d
def f061trx_f061_tax_rate_and_geography_net_tax_pos_smoothaccel_63d_sm252_3d_v086_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of net_tax_pos smoothed over 504d
def f061trx_f061_tax_rate_and_geography_net_tax_pos_smoothaccel_252d_sm504_3d_v087_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tax_to_rev smoothed over 252d
def f061trx_f061_tax_rate_and_geography_tax_to_rev_smoothaccel_63d_sm252_3d_v088_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tax_to_rev smoothed over 504d
def f061trx_f061_tax_rate_and_geography_tax_to_rev_smoothaccel_252d_sm504_3d_v089_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tax_yoy_chg smoothed over 252d
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_smoothaccel_63d_sm252_3d_v090_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tax_yoy_chg smoothed over 504d
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_smoothaccel_252d_sm504_3d_v091_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_accelz_21d_z252_3d_v092_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_accelz_63d_z504_3d_v093_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_accelz_21d_z252_3d_v094_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_accelz_63d_z504_3d_v095_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_accelz_21d_z252_3d_v096_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_accelz_63d_z504_3d_v097_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_accelz_21d_z252_3d_v098_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_accelz_63d_z504_3d_v099_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_accelz_21d_z252_3d_v100_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_accelz_63d_z504_3d_v101_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_accelz_21d_z252_3d_v102_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_accelz_63d_z504_3d_v103_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_accelz_21d_z252_3d_v104_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_accelz_63d_z504_3d_v105_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eff_tax_rate (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_signflip_63d_3d_v106_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eff_tax_rate (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_signflip_252d_3d_v107_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tax_vol_252 (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_vol_252_signflip_63d_3d_v108_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tax_vol_252 (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_vol_252_signflip_252d_3d_v109_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tax_assets_share (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_assets_share_signflip_63d_3d_v110_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tax_assets_share (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_assets_share_signflip_252d_3d_v111_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tax_liab_share (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_liab_share_signflip_63d_3d_v112_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tax_liab_share (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_liab_share_signflip_252d_3d_v113_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in net_tax_pos (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_net_tax_pos_signflip_63d_3d_v114_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in net_tax_pos (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_net_tax_pos_signflip_252d_3d_v115_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tax_to_rev (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_to_rev_signflip_63d_3d_v116_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tax_to_rev (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_to_rev_signflip_252d_3d_v117_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tax_yoy_chg (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_signflip_63d_3d_v118_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tax_yoy_chg (raw count, no price scaling)
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_signflip_252d_3d_v119_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eff_tax_rate normalized by 252d range
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_rngaccel_63d_r252_3d_v120_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eff_tax_rate normalized by 504d range
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_rngaccel_252d_r504_3d_v121_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_vol_252 normalized by 252d range
def f061trx_f061_tax_rate_and_geography_tax_vol_252_rngaccel_63d_r252_3d_v122_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_vol_252 normalized by 504d range
def f061trx_f061_tax_rate_and_geography_tax_vol_252_rngaccel_252d_r504_3d_v123_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_assets_share normalized by 252d range
def f061trx_f061_tax_rate_and_geography_tax_assets_share_rngaccel_63d_r252_3d_v124_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_assets_share normalized by 504d range
def f061trx_f061_tax_rate_and_geography_tax_assets_share_rngaccel_252d_r504_3d_v125_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_liab_share normalized by 252d range
def f061trx_f061_tax_rate_and_geography_tax_liab_share_rngaccel_63d_r252_3d_v126_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_liab_share normalized by 504d range
def f061trx_f061_tax_rate_and_geography_tax_liab_share_rngaccel_252d_r504_3d_v127_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_tax_pos normalized by 252d range
def f061trx_f061_tax_rate_and_geography_net_tax_pos_rngaccel_63d_r252_3d_v128_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_tax_pos normalized by 504d range
def f061trx_f061_tax_rate_and_geography_net_tax_pos_rngaccel_252d_r504_3d_v129_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_to_rev normalized by 252d range
def f061trx_f061_tax_rate_and_geography_tax_to_rev_rngaccel_63d_r252_3d_v130_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_to_rev normalized by 504d range
def f061trx_f061_tax_rate_and_geography_tax_to_rev_rngaccel_252d_r504_3d_v131_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_yoy_chg normalized by 252d range
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_rngaccel_63d_r252_3d_v132_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_yoy_chg normalized by 504d range
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_rngaccel_252d_r504_3d_v133_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_cumslope_21d_3d_v134_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_cumslope_63d_3d_v135_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_cumslope_252d_3d_v136_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_cumslope_21d_3d_v137_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_cumslope_63d_3d_v138_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_cumslope_252d_3d_v139_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_cumslope_21d_3d_v140_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_cumslope_63d_3d_v141_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_cumslope_252d_3d_v142_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_cumslope_21d_3d_v143_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_cumslope_63d_3d_v144_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_cumslope_252d_3d_v145_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_cumslope_21d_3d_v146_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_cumslope_63d_3d_v147_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_cumslope_252d_3d_v148_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_cumslope_21d_3d_v149_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_cumslope_63d_3d_v150_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

