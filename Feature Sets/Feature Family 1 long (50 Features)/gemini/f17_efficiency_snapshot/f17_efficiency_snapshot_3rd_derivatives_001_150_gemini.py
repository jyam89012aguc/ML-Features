import numpy as np
import pandas as pd
import inspect

def _eff_ratio(num, den): return num / den.replace(0, np.nan)
def _eff_zscore(s, w): return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

def f17_efficiency_snapshot_asset_turnover_raw_jerk(arg_revenue, arg_assets): return (_eff_ratio(arg_revenue, arg_assets)).diff().diff()
def f17_efficiency_snapshot_asset_turnover_z63_jerk(arg_revenue, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue, arg_assets), 63)).diff().diff()
def f17_efficiency_snapshot_asset_turnover_z126_jerk(arg_revenue, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue, arg_assets), 126)).diff().diff()
def f17_efficiency_snapshot_asset_turnover_z252_jerk(arg_revenue, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue, arg_assets), 252)).diff().diff()
def f17_efficiency_snapshot_asset_turnover_z504_jerk(arg_revenue, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue, arg_assets), 504)).diff().diff()
def f17_efficiency_snapshot_asset_turnover_z756_jerk(arg_revenue, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue, arg_assets), 756)).diff().diff()
def f17_efficiency_snapshot_gp_to_assets_raw_jerk(arg_gp, arg_assets): return (_eff_ratio(arg_gp, arg_assets)).diff().diff()
def f17_efficiency_snapshot_gp_to_assets_z63_jerk(arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_gp, arg_assets), 63)).diff().diff()
def f17_efficiency_snapshot_gp_to_assets_z126_jerk(arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_gp, arg_assets), 126)).diff().diff()
def f17_efficiency_snapshot_gp_to_assets_z252_jerk(arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_gp, arg_assets), 252)).diff().diff()
def f17_efficiency_snapshot_gp_to_assets_z504_jerk(arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_gp, arg_assets), 504)).diff().diff()
def f17_efficiency_snapshot_gp_to_assets_z756_jerk(arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_gp, arg_assets), 756)).diff().diff()
def f17_efficiency_snapshot_opinc_to_assets_raw_jerk(arg_opinc, arg_assets): return (_eff_ratio(arg_opinc, arg_assets)).diff().diff()
def f17_efficiency_snapshot_opinc_to_assets_z63_jerk(arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_opinc, arg_assets), 63)).diff().diff()
def f17_efficiency_snapshot_opinc_to_assets_z126_jerk(arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_opinc, arg_assets), 126)).diff().diff()
def f17_efficiency_snapshot_opinc_to_assets_z252_jerk(arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_opinc, arg_assets), 252)).diff().diff()
def f17_efficiency_snapshot_opinc_to_assets_z504_jerk(arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_opinc, arg_assets), 504)).diff().diff()
def f17_efficiency_snapshot_opinc_to_assets_z756_jerk(arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_opinc, arg_assets), 756)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_assets_raw_jerk(arg_ebitda, arg_assets): return (_eff_ratio(arg_ebitda, arg_assets)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_assets_z63_jerk(arg_ebitda, arg_assets): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets), 63)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_assets_z126_jerk(arg_ebitda, arg_assets): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets), 126)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_assets_z252_jerk(arg_ebitda, arg_assets): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets), 252)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_assets_z504_jerk(arg_ebitda, arg_assets): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets), 504)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_assets_z756_jerk(arg_ebitda, arg_assets): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets), 756)).diff().diff()
def f17_efficiency_snapshot_netinc_to_assets_raw_jerk(arg_netinc, arg_assets): return (_eff_ratio(arg_netinc, arg_assets)).diff().diff()
def f17_efficiency_snapshot_netinc_to_assets_z63_jerk(arg_netinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_netinc, arg_assets), 63)).diff().diff()
def f17_efficiency_snapshot_netinc_to_assets_z126_jerk(arg_netinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_netinc, arg_assets), 126)).diff().diff()
def f17_efficiency_snapshot_netinc_to_assets_z252_jerk(arg_netinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_netinc, arg_assets), 252)).diff().diff()
def f17_efficiency_snapshot_netinc_to_assets_z504_jerk(arg_netinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_netinc, arg_assets), 504)).diff().diff()
def f17_efficiency_snapshot_netinc_to_assets_z756_jerk(arg_netinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_netinc, arg_assets), 756)).diff().diff()
def f17_efficiency_snapshot_wc_turnover_raw_jerk(arg_revenue, arg_workingcapital): return (_eff_ratio(arg_revenue, arg_workingcapital)).diff().diff()
def f17_efficiency_snapshot_wc_turnover_z63_jerk(arg_revenue, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_revenue, arg_workingcapital), 63)).diff().diff()
def f17_efficiency_snapshot_wc_turnover_z126_jerk(arg_revenue, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_revenue, arg_workingcapital), 126)).diff().diff()
def f17_efficiency_snapshot_wc_turnover_z252_jerk(arg_revenue, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_revenue, arg_workingcapital), 252)).diff().diff()
def f17_efficiency_snapshot_wc_turnover_z504_jerk(arg_revenue, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_revenue, arg_workingcapital), 504)).diff().diff()
def f17_efficiency_snapshot_wc_turnover_z756_jerk(arg_revenue, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_revenue, arg_workingcapital), 756)).diff().diff()
def f17_efficiency_snapshot_gp_to_wc_raw_jerk(arg_gp, arg_workingcapital): return (_eff_ratio(arg_gp, arg_workingcapital)).diff().diff()
def f17_efficiency_snapshot_gp_to_wc_z63_jerk(arg_gp, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_gp, arg_workingcapital), 63)).diff().diff()
def f17_efficiency_snapshot_gp_to_wc_z126_jerk(arg_gp, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_gp, arg_workingcapital), 126)).diff().diff()
def f17_efficiency_snapshot_gp_to_wc_z252_jerk(arg_gp, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_gp, arg_workingcapital), 252)).diff().diff()
def f17_efficiency_snapshot_gp_to_wc_z504_jerk(arg_gp, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_gp, arg_workingcapital), 504)).diff().diff()
def f17_efficiency_snapshot_gp_to_wc_z756_jerk(arg_gp, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_gp, arg_workingcapital), 756)).diff().diff()
def f17_efficiency_snapshot_opinc_to_wc_raw_jerk(arg_opinc, arg_workingcapital): return (_eff_ratio(arg_opinc, arg_workingcapital)).diff().diff()
def f17_efficiency_snapshot_opinc_to_wc_z63_jerk(arg_opinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_opinc, arg_workingcapital), 63)).diff().diff()
def f17_efficiency_snapshot_opinc_to_wc_z126_jerk(arg_opinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_opinc, arg_workingcapital), 126)).diff().diff()
def f17_efficiency_snapshot_opinc_to_wc_z252_jerk(arg_opinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_opinc, arg_workingcapital), 252)).diff().diff()
def f17_efficiency_snapshot_opinc_to_wc_z504_jerk(arg_opinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_opinc, arg_workingcapital), 504)).diff().diff()
def f17_efficiency_snapshot_opinc_to_wc_z756_jerk(arg_opinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_opinc, arg_workingcapital), 756)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_wc_raw_jerk(arg_ebitda, arg_workingcapital): return (_eff_ratio(arg_ebitda, arg_workingcapital)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_wc_z63_jerk(arg_ebitda, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_workingcapital), 63)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_wc_z126_jerk(arg_ebitda, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_workingcapital), 126)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_wc_z252_jerk(arg_ebitda, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_workingcapital), 252)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_wc_z504_jerk(arg_ebitda, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_workingcapital), 504)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_wc_z756_jerk(arg_ebitda, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_workingcapital), 756)).diff().diff()
def f17_efficiency_snapshot_netinc_to_wc_raw_jerk(arg_netinc, arg_workingcapital): return (_eff_ratio(arg_netinc, arg_workingcapital)).diff().diff()
def f17_efficiency_snapshot_netinc_to_wc_z63_jerk(arg_netinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_netinc, arg_workingcapital), 63)).diff().diff()
def f17_efficiency_snapshot_netinc_to_wc_z126_jerk(arg_netinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_netinc, arg_workingcapital), 126)).diff().diff()
def f17_efficiency_snapshot_netinc_to_wc_z252_jerk(arg_netinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_netinc, arg_workingcapital), 252)).diff().diff()
def f17_efficiency_snapshot_netinc_to_wc_z504_jerk(arg_netinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_netinc, arg_workingcapital), 504)).diff().diff()
def f17_efficiency_snapshot_netinc_to_wc_z756_jerk(arg_netinc, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_netinc, arg_workingcapital), 756)).diff().diff()
def f17_efficiency_snapshot_rev_per_share_raw_jerk(arg_revenue, arg_shareswa): return (_eff_ratio(arg_revenue, arg_shareswa)).diff().diff()
def f17_efficiency_snapshot_rev_per_share_z63_jerk(arg_revenue, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_revenue, arg_shareswa), 63)).diff().diff()
def f17_efficiency_snapshot_rev_per_share_z126_jerk(arg_revenue, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_revenue, arg_shareswa), 126)).diff().diff()
def f17_efficiency_snapshot_rev_per_share_z252_jerk(arg_revenue, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_revenue, arg_shareswa), 252)).diff().diff()
def f17_efficiency_snapshot_rev_per_share_z504_jerk(arg_revenue, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_revenue, arg_shareswa), 504)).diff().diff()
def f17_efficiency_snapshot_rev_per_share_z756_jerk(arg_revenue, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_revenue, arg_shareswa), 756)).diff().diff()
def f17_efficiency_snapshot_gp_per_share_raw_jerk(arg_gp, arg_shareswa): return (_eff_ratio(arg_gp, arg_shareswa)).diff().diff()
def f17_efficiency_snapshot_gp_per_share_z63_jerk(arg_gp, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_gp, arg_shareswa), 63)).diff().diff()
def f17_efficiency_snapshot_gp_per_share_z126_jerk(arg_gp, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_gp, arg_shareswa), 126)).diff().diff()
def f17_efficiency_snapshot_gp_per_share_z252_jerk(arg_gp, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_gp, arg_shareswa), 252)).diff().diff()
def f17_efficiency_snapshot_gp_per_share_z504_jerk(arg_gp, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_gp, arg_shareswa), 504)).diff().diff()
def f17_efficiency_snapshot_gp_per_share_z756_jerk(arg_gp, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_gp, arg_shareswa), 756)).diff().diff()
def f17_efficiency_snapshot_opinc_per_share_raw_jerk(arg_opinc, arg_shareswa): return (_eff_ratio(arg_opinc, arg_shareswa)).diff().diff()
def f17_efficiency_snapshot_opinc_per_share_z63_jerk(arg_opinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_opinc, arg_shareswa), 63)).diff().diff()
def f17_efficiency_snapshot_opinc_per_share_z126_jerk(arg_opinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_opinc, arg_shareswa), 126)).diff().diff()
def f17_efficiency_snapshot_opinc_per_share_z252_jerk(arg_opinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_opinc, arg_shareswa), 252)).diff().diff()
def f17_efficiency_snapshot_opinc_per_share_z504_jerk(arg_opinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_opinc, arg_shareswa), 504)).diff().diff()
def f17_efficiency_snapshot_opinc_per_share_z756_jerk(arg_opinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_opinc, arg_shareswa), 756)).diff().diff()
def f17_efficiency_snapshot_ebitda_per_share_raw_jerk(arg_ebitda, arg_shareswa): return (_eff_ratio(arg_ebitda, arg_shareswa)).diff().diff()
def f17_efficiency_snapshot_ebitda_per_share_z63_jerk(arg_ebitda, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 63)).diff().diff()
def f17_efficiency_snapshot_ebitda_per_share_z126_jerk(arg_ebitda, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 126)).diff().diff()
def f17_efficiency_snapshot_ebitda_per_share_z252_jerk(arg_ebitda, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 252)).diff().diff()
def f17_efficiency_snapshot_ebitda_per_share_z504_jerk(arg_ebitda, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 504)).diff().diff()
def f17_efficiency_snapshot_ebitda_per_share_z756_jerk(arg_ebitda, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 756)).diff().diff()
def f17_efficiency_snapshot_netinc_per_share_raw_jerk(arg_netinc, arg_shareswa): return (_eff_ratio(arg_netinc, arg_shareswa)).diff().diff()
def f17_efficiency_snapshot_netinc_per_share_z63_jerk(arg_netinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 63)).diff().diff()
def f17_efficiency_snapshot_netinc_per_share_z126_jerk(arg_netinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 126)).diff().diff()
def f17_efficiency_snapshot_netinc_per_share_z252_jerk(arg_netinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 252)).diff().diff()
def f17_efficiency_snapshot_netinc_per_share_z504_jerk(arg_netinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 504)).diff().diff()
def f17_efficiency_snapshot_netinc_per_share_z756_jerk(arg_netinc, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 756)).diff().diff()
def f17_efficiency_snapshot_wc_to_assets_raw_jerk(arg_workingcapital, arg_assets): return (_eff_ratio(arg_workingcapital, arg_assets)).diff().diff()
def f17_efficiency_snapshot_wc_to_assets_z63_jerk(arg_workingcapital, arg_assets): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 63)).diff().diff()
def f17_efficiency_snapshot_wc_to_assets_z126_jerk(arg_workingcapital, arg_assets): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 126)).diff().diff()
def f17_efficiency_snapshot_wc_to_assets_z252_jerk(arg_workingcapital, arg_assets): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 252)).diff().diff()
def f17_efficiency_snapshot_wc_to_assets_z504_jerk(arg_workingcapital, arg_assets): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 504)).diff().diff()
def f17_efficiency_snapshot_wc_to_assets_z756_jerk(arg_workingcapital, arg_assets): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 756)).diff().diff()
def f17_efficiency_snapshot_assets_per_share_raw_jerk(arg_assets, arg_shareswa): return (_eff_ratio(arg_assets, arg_shareswa)).diff().diff()
def f17_efficiency_snapshot_assets_per_share_z63_jerk(arg_assets, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 63)).diff().diff()
def f17_efficiency_snapshot_assets_per_share_z126_jerk(arg_assets, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 126)).diff().diff()
def f17_efficiency_snapshot_assets_per_share_z252_jerk(arg_assets, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 252)).diff().diff()
def f17_efficiency_snapshot_assets_per_share_z504_jerk(arg_assets, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 504)).diff().diff()
def f17_efficiency_snapshot_assets_per_share_z756_jerk(arg_assets, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 756)).diff().diff()
def f17_efficiency_snapshot_wc_per_share_raw_jerk(arg_workingcapital, arg_shareswa): return (_eff_ratio(arg_workingcapital, arg_shareswa)).diff().diff()
def f17_efficiency_snapshot_wc_per_share_z63_jerk(arg_workingcapital, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 63)).diff().diff()
def f17_efficiency_snapshot_wc_per_share_z126_jerk(arg_workingcapital, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 126)).diff().diff()
def f17_efficiency_snapshot_wc_per_share_z252_jerk(arg_workingcapital, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 252)).diff().diff()
def f17_efficiency_snapshot_wc_per_share_z504_jerk(arg_workingcapital, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 504)).diff().diff()
def f17_efficiency_snapshot_wc_per_share_z756_jerk(arg_workingcapital, arg_shareswa): return (_eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 756)).diff().diff()
def f17_efficiency_snapshot_gp_margin_eff_raw_jerk(arg_gp, arg_revenue): return (_eff_ratio(arg_gp, arg_revenue)).diff().diff()
def f17_efficiency_snapshot_gp_margin_eff_z63_jerk(arg_gp, arg_revenue): return (_eff_zscore(_eff_ratio(arg_gp, arg_revenue), 63)).diff().diff()
def f17_efficiency_snapshot_gp_margin_eff_z126_jerk(arg_gp, arg_revenue): return (_eff_zscore(_eff_ratio(arg_gp, arg_revenue), 126)).diff().diff()
def f17_efficiency_snapshot_gp_margin_eff_z252_jerk(arg_gp, arg_revenue): return (_eff_zscore(_eff_ratio(arg_gp, arg_revenue), 252)).diff().diff()
def f17_efficiency_snapshot_gp_margin_eff_z504_jerk(arg_gp, arg_revenue): return (_eff_zscore(_eff_ratio(arg_gp, arg_revenue), 504)).diff().diff()
def f17_efficiency_snapshot_gp_margin_eff_z756_jerk(arg_gp, arg_revenue): return (_eff_zscore(_eff_ratio(arg_gp, arg_revenue), 756)).diff().diff()
def f17_efficiency_snapshot_opinc_margin_eff_raw_jerk(arg_opinc, arg_revenue): return (_eff_ratio(arg_opinc, arg_revenue)).diff().diff()
def f17_efficiency_snapshot_opinc_margin_eff_z63_jerk(arg_opinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 63)).diff().diff()
def f17_efficiency_snapshot_opinc_margin_eff_z126_jerk(arg_opinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 126)).diff().diff()
def f17_efficiency_snapshot_opinc_margin_eff_z252_jerk(arg_opinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 252)).diff().diff()
def f17_efficiency_snapshot_opinc_margin_eff_z504_jerk(arg_opinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 504)).diff().diff()
def f17_efficiency_snapshot_opinc_margin_eff_z756_jerk(arg_opinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 756)).diff().diff()
def f17_efficiency_snapshot_ebitda_margin_eff_raw_jerk(arg_ebitda, arg_revenue): return (_eff_ratio(arg_ebitda, arg_revenue)).diff().diff()
def f17_efficiency_snapshot_ebitda_margin_eff_z63_jerk(arg_ebitda, arg_revenue): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 63)).diff().diff()
def f17_efficiency_snapshot_ebitda_margin_eff_z126_jerk(arg_ebitda, arg_revenue): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 126)).diff().diff()
def f17_efficiency_snapshot_ebitda_margin_eff_z252_jerk(arg_ebitda, arg_revenue): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 252)).diff().diff()
def f17_efficiency_snapshot_ebitda_margin_eff_z504_jerk(arg_ebitda, arg_revenue): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 504)).diff().diff()
def f17_efficiency_snapshot_ebitda_margin_eff_z756_jerk(arg_ebitda, arg_revenue): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 756)).diff().diff()
def f17_efficiency_snapshot_netinc_margin_eff_raw_jerk(arg_netinc, arg_revenue): return (_eff_ratio(arg_netinc, arg_revenue)).diff().diff()
def f17_efficiency_snapshot_netinc_margin_eff_z63_jerk(arg_netinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 63)).diff().diff()
def f17_efficiency_snapshot_netinc_margin_eff_z126_jerk(arg_netinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 126)).diff().diff()
def f17_efficiency_snapshot_netinc_margin_eff_z252_jerk(arg_netinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 252)).diff().diff()
def f17_efficiency_snapshot_netinc_margin_eff_z504_jerk(arg_netinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 504)).diff().diff()
def f17_efficiency_snapshot_netinc_margin_eff_z756_jerk(arg_netinc, arg_revenue): return (_eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 756)).diff().diff()
def f17_efficiency_snapshot_cogs_to_assets_raw_jerk(arg_revenue, arg_gp, arg_assets): return (_eff_ratio(arg_revenue - arg_gp, arg_assets)).diff().diff()
def f17_efficiency_snapshot_cogs_to_assets_z63_jerk(arg_revenue, arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 63)).diff().diff()
def f17_efficiency_snapshot_cogs_to_assets_z126_jerk(arg_revenue, arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 126)).diff().diff()
def f17_efficiency_snapshot_cogs_to_assets_z252_jerk(arg_revenue, arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 252)).diff().diff()
def f17_efficiency_snapshot_cogs_to_assets_z504_jerk(arg_revenue, arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 504)).diff().diff()
def f17_efficiency_snapshot_cogs_to_assets_z756_jerk(arg_revenue, arg_gp, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 756)).diff().diff()
def f17_efficiency_snapshot_opex_to_assets_raw_jerk(arg_revenue, arg_opinc, arg_assets): return (_eff_ratio(arg_revenue - arg_opinc, arg_assets)).diff().diff()
def f17_efficiency_snapshot_opex_to_assets_z63_jerk(arg_revenue, arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 63)).diff().diff()
def f17_efficiency_snapshot_opex_to_assets_z126_jerk(arg_revenue, arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 126)).diff().diff()
def f17_efficiency_snapshot_opex_to_assets_z252_jerk(arg_revenue, arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 252)).diff().diff()
def f17_efficiency_snapshot_opex_to_assets_z504_jerk(arg_revenue, arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 504)).diff().diff()
def f17_efficiency_snapshot_opex_to_assets_z756_jerk(arg_revenue, arg_opinc, arg_assets): return (_eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 756)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_fixed_assets_raw_jerk(arg_ebitda, arg_assets, arg_workingcapital): return (_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z63_jerk(arg_ebitda, arg_assets, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 63)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z126_jerk(arg_ebitda, arg_assets, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 126)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z252_jerk(arg_ebitda, arg_assets, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 252)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z504_jerk(arg_ebitda, arg_assets, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 504)).diff().diff()
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z756_jerk(arg_ebitda, arg_assets, arg_workingcapital): return (_eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 756)).diff().diff()

F17_EFFICIENCY_SNAPSHOT_JERK_001_150_GEMINI_REGISTRY = {
    'f17_efficiency_snapshot_asset_turnover_raw_jerk': {'inputs': ['arg_revenue', 'arg_assets'], 'func': f17_efficiency_snapshot_asset_turnover_raw_jerk},
    'f17_efficiency_snapshot_asset_turnover_z63_jerk': {'inputs': ['arg_revenue', 'arg_assets'], 'func': f17_efficiency_snapshot_asset_turnover_z63_jerk},
    'f17_efficiency_snapshot_asset_turnover_z126_jerk': {'inputs': ['arg_revenue', 'arg_assets'], 'func': f17_efficiency_snapshot_asset_turnover_z126_jerk},
    'f17_efficiency_snapshot_asset_turnover_z252_jerk': {'inputs': ['arg_revenue', 'arg_assets'], 'func': f17_efficiency_snapshot_asset_turnover_z252_jerk},
    'f17_efficiency_snapshot_asset_turnover_z504_jerk': {'inputs': ['arg_revenue', 'arg_assets'], 'func': f17_efficiency_snapshot_asset_turnover_z504_jerk},
    'f17_efficiency_snapshot_asset_turnover_z756_jerk': {'inputs': ['arg_revenue', 'arg_assets'], 'func': f17_efficiency_snapshot_asset_turnover_z756_jerk},
    'f17_efficiency_snapshot_gp_to_assets_raw_jerk': {'inputs': ['arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_gp_to_assets_raw_jerk},
    'f17_efficiency_snapshot_gp_to_assets_z63_jerk': {'inputs': ['arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_gp_to_assets_z63_jerk},
    'f17_efficiency_snapshot_gp_to_assets_z126_jerk': {'inputs': ['arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_gp_to_assets_z126_jerk},
    'f17_efficiency_snapshot_gp_to_assets_z252_jerk': {'inputs': ['arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_gp_to_assets_z252_jerk},
    'f17_efficiency_snapshot_gp_to_assets_z504_jerk': {'inputs': ['arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_gp_to_assets_z504_jerk},
    'f17_efficiency_snapshot_gp_to_assets_z756_jerk': {'inputs': ['arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_gp_to_assets_z756_jerk},
    'f17_efficiency_snapshot_opinc_to_assets_raw_jerk': {'inputs': ['arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opinc_to_assets_raw_jerk},
    'f17_efficiency_snapshot_opinc_to_assets_z63_jerk': {'inputs': ['arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opinc_to_assets_z63_jerk},
    'f17_efficiency_snapshot_opinc_to_assets_z126_jerk': {'inputs': ['arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opinc_to_assets_z126_jerk},
    'f17_efficiency_snapshot_opinc_to_assets_z252_jerk': {'inputs': ['arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opinc_to_assets_z252_jerk},
    'f17_efficiency_snapshot_opinc_to_assets_z504_jerk': {'inputs': ['arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opinc_to_assets_z504_jerk},
    'f17_efficiency_snapshot_opinc_to_assets_z756_jerk': {'inputs': ['arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opinc_to_assets_z756_jerk},
    'f17_efficiency_snapshot_ebitda_to_assets_raw_jerk': {'inputs': ['arg_ebitda', 'arg_assets'], 'func': f17_efficiency_snapshot_ebitda_to_assets_raw_jerk},
    'f17_efficiency_snapshot_ebitda_to_assets_z63_jerk': {'inputs': ['arg_ebitda', 'arg_assets'], 'func': f17_efficiency_snapshot_ebitda_to_assets_z63_jerk},
    'f17_efficiency_snapshot_ebitda_to_assets_z126_jerk': {'inputs': ['arg_ebitda', 'arg_assets'], 'func': f17_efficiency_snapshot_ebitda_to_assets_z126_jerk},
    'f17_efficiency_snapshot_ebitda_to_assets_z252_jerk': {'inputs': ['arg_ebitda', 'arg_assets'], 'func': f17_efficiency_snapshot_ebitda_to_assets_z252_jerk},
    'f17_efficiency_snapshot_ebitda_to_assets_z504_jerk': {'inputs': ['arg_ebitda', 'arg_assets'], 'func': f17_efficiency_snapshot_ebitda_to_assets_z504_jerk},
    'f17_efficiency_snapshot_ebitda_to_assets_z756_jerk': {'inputs': ['arg_ebitda', 'arg_assets'], 'func': f17_efficiency_snapshot_ebitda_to_assets_z756_jerk},
    'f17_efficiency_snapshot_netinc_to_assets_raw_jerk': {'inputs': ['arg_netinc', 'arg_assets'], 'func': f17_efficiency_snapshot_netinc_to_assets_raw_jerk},
    'f17_efficiency_snapshot_netinc_to_assets_z63_jerk': {'inputs': ['arg_netinc', 'arg_assets'], 'func': f17_efficiency_snapshot_netinc_to_assets_z63_jerk},
    'f17_efficiency_snapshot_netinc_to_assets_z126_jerk': {'inputs': ['arg_netinc', 'arg_assets'], 'func': f17_efficiency_snapshot_netinc_to_assets_z126_jerk},
    'f17_efficiency_snapshot_netinc_to_assets_z252_jerk': {'inputs': ['arg_netinc', 'arg_assets'], 'func': f17_efficiency_snapshot_netinc_to_assets_z252_jerk},
    'f17_efficiency_snapshot_netinc_to_assets_z504_jerk': {'inputs': ['arg_netinc', 'arg_assets'], 'func': f17_efficiency_snapshot_netinc_to_assets_z504_jerk},
    'f17_efficiency_snapshot_netinc_to_assets_z756_jerk': {'inputs': ['arg_netinc', 'arg_assets'], 'func': f17_efficiency_snapshot_netinc_to_assets_z756_jerk},
    'f17_efficiency_snapshot_wc_turnover_raw_jerk': {'inputs': ['arg_revenue', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_wc_turnover_raw_jerk},
    'f17_efficiency_snapshot_wc_turnover_z63_jerk': {'inputs': ['arg_revenue', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_wc_turnover_z63_jerk},
    'f17_efficiency_snapshot_wc_turnover_z126_jerk': {'inputs': ['arg_revenue', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_wc_turnover_z126_jerk},
    'f17_efficiency_snapshot_wc_turnover_z252_jerk': {'inputs': ['arg_revenue', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_wc_turnover_z252_jerk},
    'f17_efficiency_snapshot_wc_turnover_z504_jerk': {'inputs': ['arg_revenue', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_wc_turnover_z504_jerk},
    'f17_efficiency_snapshot_wc_turnover_z756_jerk': {'inputs': ['arg_revenue', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_wc_turnover_z756_jerk},
    'f17_efficiency_snapshot_gp_to_wc_raw_jerk': {'inputs': ['arg_gp', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_gp_to_wc_raw_jerk},
    'f17_efficiency_snapshot_gp_to_wc_z63_jerk': {'inputs': ['arg_gp', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_gp_to_wc_z63_jerk},
    'f17_efficiency_snapshot_gp_to_wc_z126_jerk': {'inputs': ['arg_gp', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_gp_to_wc_z126_jerk},
    'f17_efficiency_snapshot_gp_to_wc_z252_jerk': {'inputs': ['arg_gp', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_gp_to_wc_z252_jerk},
    'f17_efficiency_snapshot_gp_to_wc_z504_jerk': {'inputs': ['arg_gp', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_gp_to_wc_z504_jerk},
    'f17_efficiency_snapshot_gp_to_wc_z756_jerk': {'inputs': ['arg_gp', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_gp_to_wc_z756_jerk},
    'f17_efficiency_snapshot_opinc_to_wc_raw_jerk': {'inputs': ['arg_opinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_opinc_to_wc_raw_jerk},
    'f17_efficiency_snapshot_opinc_to_wc_z63_jerk': {'inputs': ['arg_opinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_opinc_to_wc_z63_jerk},
    'f17_efficiency_snapshot_opinc_to_wc_z126_jerk': {'inputs': ['arg_opinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_opinc_to_wc_z126_jerk},
    'f17_efficiency_snapshot_opinc_to_wc_z252_jerk': {'inputs': ['arg_opinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_opinc_to_wc_z252_jerk},
    'f17_efficiency_snapshot_opinc_to_wc_z504_jerk': {'inputs': ['arg_opinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_opinc_to_wc_z504_jerk},
    'f17_efficiency_snapshot_opinc_to_wc_z756_jerk': {'inputs': ['arg_opinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_opinc_to_wc_z756_jerk},
    'f17_efficiency_snapshot_ebitda_to_wc_raw_jerk': {'inputs': ['arg_ebitda', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_wc_raw_jerk},
    'f17_efficiency_snapshot_ebitda_to_wc_z63_jerk': {'inputs': ['arg_ebitda', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_wc_z63_jerk},
    'f17_efficiency_snapshot_ebitda_to_wc_z126_jerk': {'inputs': ['arg_ebitda', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_wc_z126_jerk},
    'f17_efficiency_snapshot_ebitda_to_wc_z252_jerk': {'inputs': ['arg_ebitda', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_wc_z252_jerk},
    'f17_efficiency_snapshot_ebitda_to_wc_z504_jerk': {'inputs': ['arg_ebitda', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_wc_z504_jerk},
    'f17_efficiency_snapshot_ebitda_to_wc_z756_jerk': {'inputs': ['arg_ebitda', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_wc_z756_jerk},
    'f17_efficiency_snapshot_netinc_to_wc_raw_jerk': {'inputs': ['arg_netinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_netinc_to_wc_raw_jerk},
    'f17_efficiency_snapshot_netinc_to_wc_z63_jerk': {'inputs': ['arg_netinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_netinc_to_wc_z63_jerk},
    'f17_efficiency_snapshot_netinc_to_wc_z126_jerk': {'inputs': ['arg_netinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_netinc_to_wc_z126_jerk},
    'f17_efficiency_snapshot_netinc_to_wc_z252_jerk': {'inputs': ['arg_netinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_netinc_to_wc_z252_jerk},
    'f17_efficiency_snapshot_netinc_to_wc_z504_jerk': {'inputs': ['arg_netinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_netinc_to_wc_z504_jerk},
    'f17_efficiency_snapshot_netinc_to_wc_z756_jerk': {'inputs': ['arg_netinc', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_netinc_to_wc_z756_jerk},
    'f17_efficiency_snapshot_rev_per_share_raw_jerk': {'inputs': ['arg_revenue', 'arg_shareswa'], 'func': f17_efficiency_snapshot_rev_per_share_raw_jerk},
    'f17_efficiency_snapshot_rev_per_share_z63_jerk': {'inputs': ['arg_revenue', 'arg_shareswa'], 'func': f17_efficiency_snapshot_rev_per_share_z63_jerk},
    'f17_efficiency_snapshot_rev_per_share_z126_jerk': {'inputs': ['arg_revenue', 'arg_shareswa'], 'func': f17_efficiency_snapshot_rev_per_share_z126_jerk},
    'f17_efficiency_snapshot_rev_per_share_z252_jerk': {'inputs': ['arg_revenue', 'arg_shareswa'], 'func': f17_efficiency_snapshot_rev_per_share_z252_jerk},
    'f17_efficiency_snapshot_rev_per_share_z504_jerk': {'inputs': ['arg_revenue', 'arg_shareswa'], 'func': f17_efficiency_snapshot_rev_per_share_z504_jerk},
    'f17_efficiency_snapshot_rev_per_share_z756_jerk': {'inputs': ['arg_revenue', 'arg_shareswa'], 'func': f17_efficiency_snapshot_rev_per_share_z756_jerk},
    'f17_efficiency_snapshot_gp_per_share_raw_jerk': {'inputs': ['arg_gp', 'arg_shareswa'], 'func': f17_efficiency_snapshot_gp_per_share_raw_jerk},
    'f17_efficiency_snapshot_gp_per_share_z63_jerk': {'inputs': ['arg_gp', 'arg_shareswa'], 'func': f17_efficiency_snapshot_gp_per_share_z63_jerk},
    'f17_efficiency_snapshot_gp_per_share_z126_jerk': {'inputs': ['arg_gp', 'arg_shareswa'], 'func': f17_efficiency_snapshot_gp_per_share_z126_jerk},
    'f17_efficiency_snapshot_gp_per_share_z252_jerk': {'inputs': ['arg_gp', 'arg_shareswa'], 'func': f17_efficiency_snapshot_gp_per_share_z252_jerk},
    'f17_efficiency_snapshot_gp_per_share_z504_jerk': {'inputs': ['arg_gp', 'arg_shareswa'], 'func': f17_efficiency_snapshot_gp_per_share_z504_jerk},
    'f17_efficiency_snapshot_gp_per_share_z756_jerk': {'inputs': ['arg_gp', 'arg_shareswa'], 'func': f17_efficiency_snapshot_gp_per_share_z756_jerk},
    'f17_efficiency_snapshot_opinc_per_share_raw_jerk': {'inputs': ['arg_opinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_opinc_per_share_raw_jerk},
    'f17_efficiency_snapshot_opinc_per_share_z63_jerk': {'inputs': ['arg_opinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_opinc_per_share_z63_jerk},
    'f17_efficiency_snapshot_opinc_per_share_z126_jerk': {'inputs': ['arg_opinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_opinc_per_share_z126_jerk},
    'f17_efficiency_snapshot_opinc_per_share_z252_jerk': {'inputs': ['arg_opinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_opinc_per_share_z252_jerk},
    'f17_efficiency_snapshot_opinc_per_share_z504_jerk': {'inputs': ['arg_opinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_opinc_per_share_z504_jerk},
    'f17_efficiency_snapshot_opinc_per_share_z756_jerk': {'inputs': ['arg_opinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_opinc_per_share_z756_jerk},
    'f17_efficiency_snapshot_ebitda_per_share_raw_jerk': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_raw_jerk},
    'f17_efficiency_snapshot_ebitda_per_share_z63_jerk': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z63_jerk},
    'f17_efficiency_snapshot_ebitda_per_share_z126_jerk': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z126_jerk},
    'f17_efficiency_snapshot_ebitda_per_share_z252_jerk': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z252_jerk},
    'f17_efficiency_snapshot_ebitda_per_share_z504_jerk': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z504_jerk},
    'f17_efficiency_snapshot_ebitda_per_share_z756_jerk': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z756_jerk},
    'f17_efficiency_snapshot_netinc_per_share_raw_jerk': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_raw_jerk},
    'f17_efficiency_snapshot_netinc_per_share_z63_jerk': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z63_jerk},
    'f17_efficiency_snapshot_netinc_per_share_z126_jerk': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z126_jerk},
    'f17_efficiency_snapshot_netinc_per_share_z252_jerk': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z252_jerk},
    'f17_efficiency_snapshot_netinc_per_share_z504_jerk': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z504_jerk},
    'f17_efficiency_snapshot_netinc_per_share_z756_jerk': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z756_jerk},
    'f17_efficiency_snapshot_wc_to_assets_raw_jerk': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_raw_jerk},
    'f17_efficiency_snapshot_wc_to_assets_z63_jerk': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z63_jerk},
    'f17_efficiency_snapshot_wc_to_assets_z126_jerk': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z126_jerk},
    'f17_efficiency_snapshot_wc_to_assets_z252_jerk': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z252_jerk},
    'f17_efficiency_snapshot_wc_to_assets_z504_jerk': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z504_jerk},
    'f17_efficiency_snapshot_wc_to_assets_z756_jerk': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z756_jerk},
    'f17_efficiency_snapshot_assets_per_share_raw_jerk': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_raw_jerk},
    'f17_efficiency_snapshot_assets_per_share_z63_jerk': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z63_jerk},
    'f17_efficiency_snapshot_assets_per_share_z126_jerk': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z126_jerk},
    'f17_efficiency_snapshot_assets_per_share_z252_jerk': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z252_jerk},
    'f17_efficiency_snapshot_assets_per_share_z504_jerk': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z504_jerk},
    'f17_efficiency_snapshot_assets_per_share_z756_jerk': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z756_jerk},
    'f17_efficiency_snapshot_wc_per_share_raw_jerk': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_raw_jerk},
    'f17_efficiency_snapshot_wc_per_share_z63_jerk': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z63_jerk},
    'f17_efficiency_snapshot_wc_per_share_z126_jerk': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z126_jerk},
    'f17_efficiency_snapshot_wc_per_share_z252_jerk': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z252_jerk},
    'f17_efficiency_snapshot_wc_per_share_z504_jerk': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z504_jerk},
    'f17_efficiency_snapshot_wc_per_share_z756_jerk': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z756_jerk},
    'f17_efficiency_snapshot_gp_margin_eff_raw_jerk': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_raw_jerk},
    'f17_efficiency_snapshot_gp_margin_eff_z63_jerk': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z63_jerk},
    'f17_efficiency_snapshot_gp_margin_eff_z126_jerk': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z126_jerk},
    'f17_efficiency_snapshot_gp_margin_eff_z252_jerk': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z252_jerk},
    'f17_efficiency_snapshot_gp_margin_eff_z504_jerk': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z504_jerk},
    'f17_efficiency_snapshot_gp_margin_eff_z756_jerk': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z756_jerk},
    'f17_efficiency_snapshot_opinc_margin_eff_raw_jerk': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_raw_jerk},
    'f17_efficiency_snapshot_opinc_margin_eff_z63_jerk': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z63_jerk},
    'f17_efficiency_snapshot_opinc_margin_eff_z126_jerk': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z126_jerk},
    'f17_efficiency_snapshot_opinc_margin_eff_z252_jerk': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z252_jerk},
    'f17_efficiency_snapshot_opinc_margin_eff_z504_jerk': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z504_jerk},
    'f17_efficiency_snapshot_opinc_margin_eff_z756_jerk': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z756_jerk},
    'f17_efficiency_snapshot_ebitda_margin_eff_raw_jerk': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_raw_jerk},
    'f17_efficiency_snapshot_ebitda_margin_eff_z63_jerk': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z63_jerk},
    'f17_efficiency_snapshot_ebitda_margin_eff_z126_jerk': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z126_jerk},
    'f17_efficiency_snapshot_ebitda_margin_eff_z252_jerk': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z252_jerk},
    'f17_efficiency_snapshot_ebitda_margin_eff_z504_jerk': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z504_jerk},
    'f17_efficiency_snapshot_ebitda_margin_eff_z756_jerk': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z756_jerk},
    'f17_efficiency_snapshot_netinc_margin_eff_raw_jerk': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_raw_jerk},
    'f17_efficiency_snapshot_netinc_margin_eff_z63_jerk': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z63_jerk},
    'f17_efficiency_snapshot_netinc_margin_eff_z126_jerk': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z126_jerk},
    'f17_efficiency_snapshot_netinc_margin_eff_z252_jerk': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z252_jerk},
    'f17_efficiency_snapshot_netinc_margin_eff_z504_jerk': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z504_jerk},
    'f17_efficiency_snapshot_netinc_margin_eff_z756_jerk': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z756_jerk},
    'f17_efficiency_snapshot_cogs_to_assets_raw_jerk': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_raw_jerk},
    'f17_efficiency_snapshot_cogs_to_assets_z63_jerk': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z63_jerk},
    'f17_efficiency_snapshot_cogs_to_assets_z126_jerk': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z126_jerk},
    'f17_efficiency_snapshot_cogs_to_assets_z252_jerk': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z252_jerk},
    'f17_efficiency_snapshot_cogs_to_assets_z504_jerk': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z504_jerk},
    'f17_efficiency_snapshot_cogs_to_assets_z756_jerk': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z756_jerk},
    'f17_efficiency_snapshot_opex_to_assets_raw_jerk': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_raw_jerk},
    'f17_efficiency_snapshot_opex_to_assets_z63_jerk': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z63_jerk},
    'f17_efficiency_snapshot_opex_to_assets_z126_jerk': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z126_jerk},
    'f17_efficiency_snapshot_opex_to_assets_z252_jerk': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z252_jerk},
    'f17_efficiency_snapshot_opex_to_assets_z504_jerk': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z504_jerk},
    'f17_efficiency_snapshot_opex_to_assets_z756_jerk': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z756_jerk},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_raw_jerk': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_raw_jerk},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z63_jerk': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z63_jerk},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z126_jerk': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z126_jerk},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z252_jerk': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z252_jerk},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z504_jerk': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z504_jerk},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z756_jerk': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z756_jerk},
}

if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    N = 2000
    data = {
        'arg_revenue': pd.Series(np.random.lognormal(10, 1, N)),
        'arg_assets': pd.Series(np.random.lognormal(12, 1, N)),
        'arg_gp': pd.Series(np.random.lognormal(9, 1, N)),
        'arg_opinc': pd.Series(np.random.lognormal(8, 1, N)),
        'arg_netinc': pd.Series(np.random.lognormal(7, 1, N)),
        'arg_workingcapital': pd.Series(np.random.lognormal(8, 1, N)),
        'arg_ebitda': pd.Series(np.random.lognormal(8.5, 1, N)),
        'arg_shareswa': pd.Series(np.random.lognormal(5, 0.5, N)),
    }
    for name, info in F17_EFFICIENCY_SNAPSHOT_JERK_001_150_GEMINI_REGISTRY.items():
        inputs = [data[arg] for arg in info['inputs']]
        q = info['func'](*inputs)
        assert len(q) == N, f'{name} length mismatch'
        assert q.nunique() > 2, f'{name} constant value'
        assert q.std() > 0, f'{name} zero variance'
        print(f'Tested {name} successfully')
