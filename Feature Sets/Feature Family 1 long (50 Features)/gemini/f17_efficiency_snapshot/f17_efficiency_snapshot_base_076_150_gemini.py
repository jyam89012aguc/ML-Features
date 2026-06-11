import numpy as np
import pandas as pd
import inspect

def _eff_ratio(num, den): return num / den.replace(0, np.nan)
def _eff_zscore(s, w): return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

def f17_efficiency_snapshot_opinc_per_share_z252(arg_opinc, arg_shareswa): return _eff_zscore(_eff_ratio(arg_opinc, arg_shareswa), 252)
def f17_efficiency_snapshot_opinc_per_share_z504(arg_opinc, arg_shareswa): return _eff_zscore(_eff_ratio(arg_opinc, arg_shareswa), 504)
def f17_efficiency_snapshot_opinc_per_share_z756(arg_opinc, arg_shareswa): return _eff_zscore(_eff_ratio(arg_opinc, arg_shareswa), 756)
def f17_efficiency_snapshot_ebitda_per_share_raw(arg_ebitda, arg_shareswa): return _eff_ratio(arg_ebitda, arg_shareswa)
def f17_efficiency_snapshot_ebitda_per_share_z63(arg_ebitda, arg_shareswa): return _eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 63)
def f17_efficiency_snapshot_ebitda_per_share_z126(arg_ebitda, arg_shareswa): return _eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 126)
def f17_efficiency_snapshot_ebitda_per_share_z252(arg_ebitda, arg_shareswa): return _eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 252)
def f17_efficiency_snapshot_ebitda_per_share_z504(arg_ebitda, arg_shareswa): return _eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 504)
def f17_efficiency_snapshot_ebitda_per_share_z756(arg_ebitda, arg_shareswa): return _eff_zscore(_eff_ratio(arg_ebitda, arg_shareswa), 756)
def f17_efficiency_snapshot_netinc_per_share_raw(arg_netinc, arg_shareswa): return _eff_ratio(arg_netinc, arg_shareswa)
def f17_efficiency_snapshot_netinc_per_share_z63(arg_netinc, arg_shareswa): return _eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 63)
def f17_efficiency_snapshot_netinc_per_share_z126(arg_netinc, arg_shareswa): return _eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 126)
def f17_efficiency_snapshot_netinc_per_share_z252(arg_netinc, arg_shareswa): return _eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 252)
def f17_efficiency_snapshot_netinc_per_share_z504(arg_netinc, arg_shareswa): return _eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 504)
def f17_efficiency_snapshot_netinc_per_share_z756(arg_netinc, arg_shareswa): return _eff_zscore(_eff_ratio(arg_netinc, arg_shareswa), 756)
def f17_efficiency_snapshot_wc_to_assets_raw(arg_workingcapital, arg_assets): return _eff_ratio(arg_workingcapital, arg_assets)
def f17_efficiency_snapshot_wc_to_assets_z63(arg_workingcapital, arg_assets): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 63)
def f17_efficiency_snapshot_wc_to_assets_z126(arg_workingcapital, arg_assets): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 126)
def f17_efficiency_snapshot_wc_to_assets_z252(arg_workingcapital, arg_assets): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 252)
def f17_efficiency_snapshot_wc_to_assets_z504(arg_workingcapital, arg_assets): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 504)
def f17_efficiency_snapshot_wc_to_assets_z756(arg_workingcapital, arg_assets): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_assets), 756)
def f17_efficiency_snapshot_assets_per_share_raw(arg_assets, arg_shareswa): return _eff_ratio(arg_assets, arg_shareswa)
def f17_efficiency_snapshot_assets_per_share_z63(arg_assets, arg_shareswa): return _eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 63)
def f17_efficiency_snapshot_assets_per_share_z126(arg_assets, arg_shareswa): return _eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 126)
def f17_efficiency_snapshot_assets_per_share_z252(arg_assets, arg_shareswa): return _eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 252)
def f17_efficiency_snapshot_assets_per_share_z504(arg_assets, arg_shareswa): return _eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 504)
def f17_efficiency_snapshot_assets_per_share_z756(arg_assets, arg_shareswa): return _eff_zscore(_eff_ratio(arg_assets, arg_shareswa), 756)
def f17_efficiency_snapshot_wc_per_share_raw(arg_workingcapital, arg_shareswa): return _eff_ratio(arg_workingcapital, arg_shareswa)
def f17_efficiency_snapshot_wc_per_share_z63(arg_workingcapital, arg_shareswa): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 63)
def f17_efficiency_snapshot_wc_per_share_z126(arg_workingcapital, arg_shareswa): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 126)
def f17_efficiency_snapshot_wc_per_share_z252(arg_workingcapital, arg_shareswa): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 252)
def f17_efficiency_snapshot_wc_per_share_z504(arg_workingcapital, arg_shareswa): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 504)
def f17_efficiency_snapshot_wc_per_share_z756(arg_workingcapital, arg_shareswa): return _eff_zscore(_eff_ratio(arg_workingcapital, arg_shareswa), 756)
def f17_efficiency_snapshot_gp_margin_eff_raw(arg_gp, arg_revenue): return _eff_ratio(arg_gp, arg_revenue)
def f17_efficiency_snapshot_gp_margin_eff_z63(arg_gp, arg_revenue): return _eff_zscore(_eff_ratio(arg_gp, arg_revenue), 63)
def f17_efficiency_snapshot_gp_margin_eff_z126(arg_gp, arg_revenue): return _eff_zscore(_eff_ratio(arg_gp, arg_revenue), 126)
def f17_efficiency_snapshot_gp_margin_eff_z252(arg_gp, arg_revenue): return _eff_zscore(_eff_ratio(arg_gp, arg_revenue), 252)
def f17_efficiency_snapshot_gp_margin_eff_z504(arg_gp, arg_revenue): return _eff_zscore(_eff_ratio(arg_gp, arg_revenue), 504)
def f17_efficiency_snapshot_gp_margin_eff_z756(arg_gp, arg_revenue): return _eff_zscore(_eff_ratio(arg_gp, arg_revenue), 756)
def f17_efficiency_snapshot_opinc_margin_eff_raw(arg_opinc, arg_revenue): return _eff_ratio(arg_opinc, arg_revenue)
def f17_efficiency_snapshot_opinc_margin_eff_z63(arg_opinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 63)
def f17_efficiency_snapshot_opinc_margin_eff_z126(arg_opinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 126)
def f17_efficiency_snapshot_opinc_margin_eff_z252(arg_opinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 252)
def f17_efficiency_snapshot_opinc_margin_eff_z504(arg_opinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 504)
def f17_efficiency_snapshot_opinc_margin_eff_z756(arg_opinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_opinc, arg_revenue), 756)
def f17_efficiency_snapshot_ebitda_margin_eff_raw(arg_ebitda, arg_revenue): return _eff_ratio(arg_ebitda, arg_revenue)
def f17_efficiency_snapshot_ebitda_margin_eff_z63(arg_ebitda, arg_revenue): return _eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 63)
def f17_efficiency_snapshot_ebitda_margin_eff_z126(arg_ebitda, arg_revenue): return _eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 126)
def f17_efficiency_snapshot_ebitda_margin_eff_z252(arg_ebitda, arg_revenue): return _eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 252)
def f17_efficiency_snapshot_ebitda_margin_eff_z504(arg_ebitda, arg_revenue): return _eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 504)
def f17_efficiency_snapshot_ebitda_margin_eff_z756(arg_ebitda, arg_revenue): return _eff_zscore(_eff_ratio(arg_ebitda, arg_revenue), 756)
def f17_efficiency_snapshot_netinc_margin_eff_raw(arg_netinc, arg_revenue): return _eff_ratio(arg_netinc, arg_revenue)
def f17_efficiency_snapshot_netinc_margin_eff_z63(arg_netinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 63)
def f17_efficiency_snapshot_netinc_margin_eff_z126(arg_netinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 126)
def f17_efficiency_snapshot_netinc_margin_eff_z252(arg_netinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 252)
def f17_efficiency_snapshot_netinc_margin_eff_z504(arg_netinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 504)
def f17_efficiency_snapshot_netinc_margin_eff_z756(arg_netinc, arg_revenue): return _eff_zscore(_eff_ratio(arg_netinc, arg_revenue), 756)
def f17_efficiency_snapshot_cogs_to_assets_raw(arg_revenue, arg_gp, arg_assets): return _eff_ratio(arg_revenue - arg_gp, arg_assets)
def f17_efficiency_snapshot_cogs_to_assets_z63(arg_revenue, arg_gp, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 63)
def f17_efficiency_snapshot_cogs_to_assets_z126(arg_revenue, arg_gp, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 126)
def f17_efficiency_snapshot_cogs_to_assets_z252(arg_revenue, arg_gp, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 252)
def f17_efficiency_snapshot_cogs_to_assets_z504(arg_revenue, arg_gp, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 504)
def f17_efficiency_snapshot_cogs_to_assets_z756(arg_revenue, arg_gp, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_gp, arg_assets), 756)
def f17_efficiency_snapshot_opex_to_assets_raw(arg_revenue, arg_opinc, arg_assets): return _eff_ratio(arg_revenue - arg_opinc, arg_assets)
def f17_efficiency_snapshot_opex_to_assets_z63(arg_revenue, arg_opinc, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 63)
def f17_efficiency_snapshot_opex_to_assets_z126(arg_revenue, arg_opinc, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 126)
def f17_efficiency_snapshot_opex_to_assets_z252(arg_revenue, arg_opinc, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 252)
def f17_efficiency_snapshot_opex_to_assets_z504(arg_revenue, arg_opinc, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 504)
def f17_efficiency_snapshot_opex_to_assets_z756(arg_revenue, arg_opinc, arg_assets): return _eff_zscore(_eff_ratio(arg_revenue - arg_opinc, arg_assets), 756)
def f17_efficiency_snapshot_ebitda_to_fixed_assets_raw(arg_ebitda, arg_assets, arg_workingcapital): return _eff_ratio(arg_ebitda, arg_assets - arg_workingcapital)
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z63(arg_ebitda, arg_assets, arg_workingcapital): return _eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 63)
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z126(arg_ebitda, arg_assets, arg_workingcapital): return _eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 126)
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z252(arg_ebitda, arg_assets, arg_workingcapital): return _eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 252)
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z504(arg_ebitda, arg_assets, arg_workingcapital): return _eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 504)
def f17_efficiency_snapshot_ebitda_to_fixed_assets_z756(arg_ebitda, arg_assets, arg_workingcapital): return _eff_zscore(_eff_ratio(arg_ebitda, arg_assets - arg_workingcapital), 756)

F17_EFFICIENCY_SNAPSHOT_BASE_076_150_GEMINI_REGISTRY = {
    'f17_efficiency_snapshot_opinc_per_share_z252': {'inputs': ['arg_opinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_opinc_per_share_z252},
    'f17_efficiency_snapshot_opinc_per_share_z504': {'inputs': ['arg_opinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_opinc_per_share_z504},
    'f17_efficiency_snapshot_opinc_per_share_z756': {'inputs': ['arg_opinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_opinc_per_share_z756},
    'f17_efficiency_snapshot_ebitda_per_share_raw': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_raw},
    'f17_efficiency_snapshot_ebitda_per_share_z63': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z63},
    'f17_efficiency_snapshot_ebitda_per_share_z126': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z126},
    'f17_efficiency_snapshot_ebitda_per_share_z252': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z252},
    'f17_efficiency_snapshot_ebitda_per_share_z504': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z504},
    'f17_efficiency_snapshot_ebitda_per_share_z756': {'inputs': ['arg_ebitda', 'arg_shareswa'], 'func': f17_efficiency_snapshot_ebitda_per_share_z756},
    'f17_efficiency_snapshot_netinc_per_share_raw': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_raw},
    'f17_efficiency_snapshot_netinc_per_share_z63': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z63},
    'f17_efficiency_snapshot_netinc_per_share_z126': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z126},
    'f17_efficiency_snapshot_netinc_per_share_z252': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z252},
    'f17_efficiency_snapshot_netinc_per_share_z504': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z504},
    'f17_efficiency_snapshot_netinc_per_share_z756': {'inputs': ['arg_netinc', 'arg_shareswa'], 'func': f17_efficiency_snapshot_netinc_per_share_z756},
    'f17_efficiency_snapshot_wc_to_assets_raw': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_raw},
    'f17_efficiency_snapshot_wc_to_assets_z63': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z63},
    'f17_efficiency_snapshot_wc_to_assets_z126': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z126},
    'f17_efficiency_snapshot_wc_to_assets_z252': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z252},
    'f17_efficiency_snapshot_wc_to_assets_z504': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z504},
    'f17_efficiency_snapshot_wc_to_assets_z756': {'inputs': ['arg_workingcapital', 'arg_assets'], 'func': f17_efficiency_snapshot_wc_to_assets_z756},
    'f17_efficiency_snapshot_assets_per_share_raw': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_raw},
    'f17_efficiency_snapshot_assets_per_share_z63': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z63},
    'f17_efficiency_snapshot_assets_per_share_z126': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z126},
    'f17_efficiency_snapshot_assets_per_share_z252': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z252},
    'f17_efficiency_snapshot_assets_per_share_z504': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z504},
    'f17_efficiency_snapshot_assets_per_share_z756': {'inputs': ['arg_assets', 'arg_shareswa'], 'func': f17_efficiency_snapshot_assets_per_share_z756},
    'f17_efficiency_snapshot_wc_per_share_raw': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_raw},
    'f17_efficiency_snapshot_wc_per_share_z63': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z63},
    'f17_efficiency_snapshot_wc_per_share_z126': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z126},
    'f17_efficiency_snapshot_wc_per_share_z252': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z252},
    'f17_efficiency_snapshot_wc_per_share_z504': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z504},
    'f17_efficiency_snapshot_wc_per_share_z756': {'inputs': ['arg_workingcapital', 'arg_shareswa'], 'func': f17_efficiency_snapshot_wc_per_share_z756},
    'f17_efficiency_snapshot_gp_margin_eff_raw': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_raw},
    'f17_efficiency_snapshot_gp_margin_eff_z63': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z63},
    'f17_efficiency_snapshot_gp_margin_eff_z126': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z126},
    'f17_efficiency_snapshot_gp_margin_eff_z252': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z252},
    'f17_efficiency_snapshot_gp_margin_eff_z504': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z504},
    'f17_efficiency_snapshot_gp_margin_eff_z756': {'inputs': ['arg_gp', 'arg_revenue'], 'func': f17_efficiency_snapshot_gp_margin_eff_z756},
    'f17_efficiency_snapshot_opinc_margin_eff_raw': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_raw},
    'f17_efficiency_snapshot_opinc_margin_eff_z63': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z63},
    'f17_efficiency_snapshot_opinc_margin_eff_z126': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z126},
    'f17_efficiency_snapshot_opinc_margin_eff_z252': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z252},
    'f17_efficiency_snapshot_opinc_margin_eff_z504': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z504},
    'f17_efficiency_snapshot_opinc_margin_eff_z756': {'inputs': ['arg_opinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_opinc_margin_eff_z756},
    'f17_efficiency_snapshot_ebitda_margin_eff_raw': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_raw},
    'f17_efficiency_snapshot_ebitda_margin_eff_z63': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z63},
    'f17_efficiency_snapshot_ebitda_margin_eff_z126': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z126},
    'f17_efficiency_snapshot_ebitda_margin_eff_z252': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z252},
    'f17_efficiency_snapshot_ebitda_margin_eff_z504': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z504},
    'f17_efficiency_snapshot_ebitda_margin_eff_z756': {'inputs': ['arg_ebitda', 'arg_revenue'], 'func': f17_efficiency_snapshot_ebitda_margin_eff_z756},
    'f17_efficiency_snapshot_netinc_margin_eff_raw': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_raw},
    'f17_efficiency_snapshot_netinc_margin_eff_z63': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z63},
    'f17_efficiency_snapshot_netinc_margin_eff_z126': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z126},
    'f17_efficiency_snapshot_netinc_margin_eff_z252': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z252},
    'f17_efficiency_snapshot_netinc_margin_eff_z504': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z504},
    'f17_efficiency_snapshot_netinc_margin_eff_z756': {'inputs': ['arg_netinc', 'arg_revenue'], 'func': f17_efficiency_snapshot_netinc_margin_eff_z756},
    'f17_efficiency_snapshot_cogs_to_assets_raw': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_raw},
    'f17_efficiency_snapshot_cogs_to_assets_z63': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z63},
    'f17_efficiency_snapshot_cogs_to_assets_z126': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z126},
    'f17_efficiency_snapshot_cogs_to_assets_z252': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z252},
    'f17_efficiency_snapshot_cogs_to_assets_z504': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z504},
    'f17_efficiency_snapshot_cogs_to_assets_z756': {'inputs': ['arg_revenue', 'arg_gp', 'arg_assets'], 'func': f17_efficiency_snapshot_cogs_to_assets_z756},
    'f17_efficiency_snapshot_opex_to_assets_raw': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_raw},
    'f17_efficiency_snapshot_opex_to_assets_z63': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z63},
    'f17_efficiency_snapshot_opex_to_assets_z126': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z126},
    'f17_efficiency_snapshot_opex_to_assets_z252': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z252},
    'f17_efficiency_snapshot_opex_to_assets_z504': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z504},
    'f17_efficiency_snapshot_opex_to_assets_z756': {'inputs': ['arg_revenue', 'arg_opinc', 'arg_assets'], 'func': f17_efficiency_snapshot_opex_to_assets_z756},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_raw': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_raw},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z63': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z63},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z126': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z126},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z252': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z252},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z504': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z504},
    'f17_efficiency_snapshot_ebitda_to_fixed_assets_z756': {'inputs': ['arg_ebitda', 'arg_assets', 'arg_workingcapital'], 'func': f17_efficiency_snapshot_ebitda_to_fixed_assets_z756},
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
    for name, info in F17_EFFICIENCY_SNAPSHOT_BASE_076_150_GEMINI_REGISTRY.items():
        inputs = [data[arg] for arg in info['inputs']]
        q = info['func'](*inputs)
        assert len(q) == N, f'{name} length mismatch'
        assert q.nunique() > 2, f'{name} constant value'
        assert q.std() > 0, f'{name} zero variance'
        print(f'Tested {name} successfully')
