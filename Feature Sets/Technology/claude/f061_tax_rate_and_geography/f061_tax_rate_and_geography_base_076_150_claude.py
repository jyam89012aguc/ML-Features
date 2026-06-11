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


# 63d z-score of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_z_63d_base_v076_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_z_126d_base_v077_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_z_252d_base_v078_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_z_504d_base_v079_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_z_63d_base_v080_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_z_126d_base_v081_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_z_252d_base_v082_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_z_504d_base_v083_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_z_63d_base_v084_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_z_126d_base_v085_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_z_252d_base_v086_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_z_504d_base_v087_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_z_63d_base_v088_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_z_126d_base_v089_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_z_252d_base_v090_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_z_504d_base_v091_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_z_63d_base_v092_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_z_126d_base_v093_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_z_252d_base_v094_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_z_504d_base_v095_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_z_63d_base_v096_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_z_126d_base_v097_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_z_252d_base_v098_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_z_504d_base_v099_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_z_63d_base_v100_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_z_126d_base_v101_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_z_252d_base_v102_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_z_504d_base_v103_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_distmax_252d_base_v104_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_distmax_504d_base_v105_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_distmax_252d_base_v106_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_distmax_504d_base_v107_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_distmax_252d_base_v108_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_distmax_504d_base_v109_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_distmax_252d_base_v110_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_distmax_504d_base_v111_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_distmax_252d_base_v112_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_distmax_504d_base_v113_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_distmax_252d_base_v114_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_distmax_504d_base_v115_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_distmax_252d_base_v116_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_distmax_504d_base_v117_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_distmed_126d_base_v118_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_distmed_252d_base_v119_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_distmed_504d_base_v120_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_distmed_126d_base_v121_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_distmed_252d_base_v122_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_distmed_504d_base_v123_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_distmed_126d_base_v124_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_distmed_252d_base_v125_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_distmed_504d_base_v126_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_distmed_126d_base_v127_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_distmed_252d_base_v128_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_distmed_504d_base_v129_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_distmed_126d_base_v130_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_distmed_252d_base_v131_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_distmed_504d_base_v132_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_distmed_126d_base_v133_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_distmed_252d_base_v134_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_distmed_504d_base_v135_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_distmed_126d_base_v136_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_distmed_252d_base_v137_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_distmed_504d_base_v138_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_chg_63d_base_v139_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_chg_252d_base_v140_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_chg_63d_base_v141_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_chg_252d_base_v142_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_chg_63d_base_v143_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_chg_252d_base_v144_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_chg_63d_base_v145_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_chg_252d_base_v146_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_chg_63d_base_v147_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_chg_252d_base_v148_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_chg_63d_base_v149_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_chg_252d_base_v150_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

