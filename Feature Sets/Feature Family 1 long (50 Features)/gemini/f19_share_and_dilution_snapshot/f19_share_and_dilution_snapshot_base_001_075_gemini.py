# f19_share_and_dilution_snapshot_base_001_075_gemini.py
import pandas as pd
import numpy as np
import inspect
import sys

def _sd_level(s): return np.log1p(s.clip(lower=0))
def _sd_ratio(num, den): return num / den.replace(0, np.nan)
def f19_share_and_dilution_snapshot_shareswa_log_63_arg_shareswa(arg_shareswa): return _sd_level(arg_shareswa.rolling(63).mean())
def f19_share_and_dilution_snapshot_sharesbas_log_63_arg_sharesbas(arg_sharesbas): return _sd_level(arg_sharesbas.rolling(63).mean())
def f19_share_and_dilution_snapshot_dilution_factor_63_arg_shareswa_arg_sharesbas(arg_shareswa, arg_sharesbas): return _sd_ratio(arg_shareswa, arg_sharesbas).rolling(63).mean()
def f19_share_and_dilution_snapshot_price_per_wa_63_arg_marketcap_arg_shareswa(arg_marketcap, arg_shareswa): return _sd_ratio(arg_marketcap, arg_shareswa).rolling(63).mean()
def f19_share_and_dilution_snapshot_equity_per_wa_63_arg_equity_arg_shareswa(arg_equity, arg_shareswa): return _sd_ratio(arg_equity, arg_shareswa).rolling(63).mean()
def f19_share_and_dilution_snapshot_netinc_per_wa_63_arg_netinc_arg_shareswa(arg_netinc, arg_shareswa): return _sd_ratio(arg_netinc, arg_shareswa).rolling(63).mean()
def f19_share_and_dilution_snapshot_revenue_per_wa_63_arg_revenue_arg_shareswa(arg_revenue, arg_shareswa): return _sd_ratio(arg_revenue, arg_shareswa).rolling(63).mean()
def f19_share_and_dilution_snapshot_shareswa_rel_mean_63_arg_shareswa(arg_shareswa): return _sd_ratio(arg_shareswa, arg_shareswa.rolling(63).mean())
def f19_share_and_dilution_snapshot_sharesbas_rel_mean_63_arg_sharesbas(arg_sharesbas): return _sd_ratio(arg_sharesbas, arg_sharesbas.rolling(63).mean())
def f19_share_and_dilution_snapshot_shareswa_zscore_63_arg_shareswa(arg_shareswa): return (arg_shareswa - arg_shareswa.rolling(63).mean()) / (arg_shareswa.rolling(63).std() + 1e-8)
def f19_share_and_dilution_snapshot_sharesbas_zscore_63_arg_sharesbas(arg_sharesbas): return (arg_sharesbas - arg_sharesbas.rolling(63).mean()) / (arg_sharesbas.rolling(63).std() + 1e-8)
def f19_share_and_dilution_snapshot_dilution_zscore_63_arg_shareswa_arg_sharesbas(arg_shareswa, arg_sharesbas): return (q := _sd_ratio(arg_shareswa, arg_sharesbas), (q - q.rolling(63).mean()) / (q.rolling(63).std() + 1e-8))[1]
def f19_share_and_dilution_snapshot_shareswa_pct_change_63_arg_shareswa(arg_shareswa): return arg_shareswa.pct_change(63)
def f19_share_and_dilution_snapshot_sharesbas_pct_change_63_arg_sharesbas(arg_sharesbas): return arg_sharesbas.pct_change(63)
def f19_share_and_dilution_snapshot_dilution_factor_change_63_arg_shareswa_arg_sharesbas(arg_shareswa, arg_sharesbas): return _sd_ratio(arg_shareswa, arg_sharesbas).pct_change(63)
def f19_share_and_dilution_snapshot_marketcap_to_equity_63_arg_marketcap_arg_equity(arg_marketcap, arg_equity): return _sd_ratio(arg_marketcap, arg_equity).rolling(63).mean()
def f19_share_and_dilution_snapshot_netinc_to_revenue_63_arg_netinc_arg_revenue(arg_netinc, arg_revenue): return _sd_ratio(arg_netinc, arg_revenue).rolling(63).mean()
def f19_share_and_dilution_snapshot_shareswa_to_revenue_63_arg_shareswa_arg_revenue(arg_shareswa, arg_revenue): return _sd_ratio(arg_shareswa, arg_revenue).rolling(63).mean()
def f19_share_and_dilution_snapshot_shareswa_to_equity_63_arg_shareswa_arg_equity(arg_shareswa, arg_equity): return _sd_ratio(arg_shareswa, arg_equity).rolling(63).mean()
def f19_share_and_dilution_snapshot_shareswa_dist_max_63_arg_shareswa(arg_shareswa): return arg_shareswa / (arg_shareswa.rolling(63).max() + 1e-8)
def f19_share_and_dilution_snapshot_shareswa_dist_min_63_arg_shareswa(arg_shareswa): return arg_shareswa / (arg_shareswa.rolling(63).min() + 1e-8)
def f19_share_and_dilution_snapshot_sharesbas_dist_max_63_arg_sharesbas(arg_sharesbas): return arg_sharesbas / (arg_sharesbas.rolling(63).max() + 1e-8)
def f19_share_and_dilution_snapshot_sharesbas_dist_min_63_arg_sharesbas(arg_sharesbas): return arg_sharesbas / (arg_sharesbas.rolling(63).min() + 1e-8)
def f19_share_and_dilution_snapshot_shareswa_growth_accel_63_arg_shareswa(arg_shareswa): return arg_shareswa.pct_change(63).diff(63)
def f19_share_and_dilution_snapshot_sharesbas_growth_accel_63_arg_sharesbas(arg_sharesbas): return arg_sharesbas.pct_change(63).diff(63)
def f19_share_and_dilution_snapshot_shareswa_log_126_arg_shareswa(arg_shareswa): return _sd_level(arg_shareswa.rolling(126).mean())
def f19_share_and_dilution_snapshot_sharesbas_log_126_arg_sharesbas(arg_sharesbas): return _sd_level(arg_sharesbas.rolling(126).mean())
def f19_share_and_dilution_snapshot_dilution_factor_126_arg_shareswa_arg_sharesbas(arg_shareswa, arg_sharesbas): return _sd_ratio(arg_shareswa, arg_sharesbas).rolling(126).mean()
def f19_share_and_dilution_snapshot_price_per_wa_126_arg_marketcap_arg_shareswa(arg_marketcap, arg_shareswa): return _sd_ratio(arg_marketcap, arg_shareswa).rolling(126).mean()
def f19_share_and_dilution_snapshot_equity_per_wa_126_arg_equity_arg_shareswa(arg_equity, arg_shareswa): return _sd_ratio(arg_equity, arg_shareswa).rolling(126).mean()
def f19_share_and_dilution_snapshot_netinc_per_wa_126_arg_netinc_arg_shareswa(arg_netinc, arg_shareswa): return _sd_ratio(arg_netinc, arg_shareswa).rolling(126).mean()
def f19_share_and_dilution_snapshot_revenue_per_wa_126_arg_revenue_arg_shareswa(arg_revenue, arg_shareswa): return _sd_ratio(arg_revenue, arg_shareswa).rolling(126).mean()
def f19_share_and_dilution_snapshot_shareswa_rel_mean_126_arg_shareswa(arg_shareswa): return _sd_ratio(arg_shareswa, arg_shareswa.rolling(126).mean())
def f19_share_and_dilution_snapshot_sharesbas_rel_mean_126_arg_sharesbas(arg_sharesbas): return _sd_ratio(arg_sharesbas, arg_sharesbas.rolling(126).mean())
def f19_share_and_dilution_snapshot_shareswa_zscore_126_arg_shareswa(arg_shareswa): return (arg_shareswa - arg_shareswa.rolling(126).mean()) / (arg_shareswa.rolling(126).std() + 1e-8)
def f19_share_and_dilution_snapshot_sharesbas_zscore_126_arg_sharesbas(arg_sharesbas): return (arg_sharesbas - arg_sharesbas.rolling(126).mean()) / (arg_sharesbas.rolling(126).std() + 1e-8)
def f19_share_and_dilution_snapshot_dilution_zscore_126_arg_shareswa_arg_sharesbas(arg_shareswa, arg_sharesbas): return (q := _sd_ratio(arg_shareswa, arg_sharesbas), (q - q.rolling(126).mean()) / (q.rolling(126).std() + 1e-8))[1]
def f19_share_and_dilution_snapshot_shareswa_pct_change_126_arg_shareswa(arg_shareswa): return arg_shareswa.pct_change(126)
def f19_share_and_dilution_snapshot_sharesbas_pct_change_126_arg_sharesbas(arg_sharesbas): return arg_sharesbas.pct_change(126)
def f19_share_and_dilution_snapshot_dilution_factor_change_126_arg_shareswa_arg_sharesbas(arg_shareswa, arg_sharesbas): return _sd_ratio(arg_shareswa, arg_sharesbas).pct_change(126)
def f19_share_and_dilution_snapshot_marketcap_to_equity_126_arg_marketcap_arg_equity(arg_marketcap, arg_equity): return _sd_ratio(arg_marketcap, arg_equity).rolling(126).mean()
def f19_share_and_dilution_snapshot_netinc_to_revenue_126_arg_netinc_arg_revenue(arg_netinc, arg_revenue): return _sd_ratio(arg_netinc, arg_revenue).rolling(126).mean()
def f19_share_and_dilution_snapshot_shareswa_to_revenue_126_arg_shareswa_arg_revenue(arg_shareswa, arg_revenue): return _sd_ratio(arg_shareswa, arg_revenue).rolling(126).mean()
def f19_share_and_dilution_snapshot_shareswa_to_equity_126_arg_shareswa_arg_equity(arg_shareswa, arg_equity): return _sd_ratio(arg_shareswa, arg_equity).rolling(126).mean()
def f19_share_and_dilution_snapshot_shareswa_dist_max_126_arg_shareswa(arg_shareswa): return arg_shareswa / (arg_shareswa.rolling(126).max() + 1e-8)
def f19_share_and_dilution_snapshot_shareswa_dist_min_126_arg_shareswa(arg_shareswa): return arg_shareswa / (arg_shareswa.rolling(126).min() + 1e-8)
def f19_share_and_dilution_snapshot_sharesbas_dist_max_126_arg_sharesbas(arg_sharesbas): return arg_sharesbas / (arg_sharesbas.rolling(126).max() + 1e-8)
def f19_share_and_dilution_snapshot_sharesbas_dist_min_126_arg_sharesbas(arg_sharesbas): return arg_sharesbas / (arg_sharesbas.rolling(126).min() + 1e-8)
def f19_share_and_dilution_snapshot_shareswa_growth_accel_126_arg_shareswa(arg_shareswa): return arg_shareswa.pct_change(126).diff(126)
def f19_share_and_dilution_snapshot_sharesbas_growth_accel_126_arg_sharesbas(arg_sharesbas): return arg_sharesbas.pct_change(126).diff(126)
def f19_share_and_dilution_snapshot_shareswa_log_252_arg_shareswa(arg_shareswa): return _sd_level(arg_shareswa.rolling(252).mean())
def f19_share_and_dilution_snapshot_sharesbas_log_252_arg_sharesbas(arg_sharesbas): return _sd_level(arg_sharesbas.rolling(252).mean())
def f19_share_and_dilution_snapshot_dilution_factor_252_arg_shareswa_arg_sharesbas(arg_shareswa, arg_sharesbas): return _sd_ratio(arg_shareswa, arg_sharesbas).rolling(252).mean()
def f19_share_and_dilution_snapshot_price_per_wa_252_arg_marketcap_arg_shareswa(arg_marketcap, arg_shareswa): return _sd_ratio(arg_marketcap, arg_shareswa).rolling(252).mean()
def f19_share_and_dilution_snapshot_equity_per_wa_252_arg_equity_arg_shareswa(arg_equity, arg_shareswa): return _sd_ratio(arg_equity, arg_shareswa).rolling(252).mean()
def f19_share_and_dilution_snapshot_netinc_per_wa_252_arg_netinc_arg_shareswa(arg_netinc, arg_shareswa): return _sd_ratio(arg_netinc, arg_shareswa).rolling(252).mean()
def f19_share_and_dilution_snapshot_revenue_per_wa_252_arg_revenue_arg_shareswa(arg_revenue, arg_shareswa): return _sd_ratio(arg_revenue, arg_shareswa).rolling(252).mean()
def f19_share_and_dilution_snapshot_shareswa_rel_mean_252_arg_shareswa(arg_shareswa): return _sd_ratio(arg_shareswa, arg_shareswa.rolling(252).mean())
def f19_share_and_dilution_snapshot_sharesbas_rel_mean_252_arg_sharesbas(arg_sharesbas): return _sd_ratio(arg_sharesbas, arg_sharesbas.rolling(252).mean())
def f19_share_and_dilution_snapshot_shareswa_zscore_252_arg_shareswa(arg_shareswa): return (arg_shareswa - arg_shareswa.rolling(252).mean()) / (arg_shareswa.rolling(252).std() + 1e-8)
def f19_share_and_dilution_snapshot_sharesbas_zscore_252_arg_sharesbas(arg_sharesbas): return (arg_sharesbas - arg_sharesbas.rolling(252).mean()) / (arg_sharesbas.rolling(252).std() + 1e-8)
def f19_share_and_dilution_snapshot_dilution_zscore_252_arg_shareswa_arg_sharesbas(arg_shareswa, arg_sharesbas): return (q := _sd_ratio(arg_shareswa, arg_sharesbas), (q - q.rolling(252).mean()) / (q.rolling(252).std() + 1e-8))[1]
def f19_share_and_dilution_snapshot_shareswa_pct_change_252_arg_shareswa(arg_shareswa): return arg_shareswa.pct_change(252)
def f19_share_and_dilution_snapshot_sharesbas_pct_change_252_arg_sharesbas(arg_sharesbas): return arg_sharesbas.pct_change(252)
def f19_share_and_dilution_snapshot_dilution_factor_change_252_arg_shareswa_arg_sharesbas(arg_shareswa, arg_sharesbas): return _sd_ratio(arg_shareswa, arg_sharesbas).pct_change(252)
def f19_share_and_dilution_snapshot_marketcap_to_equity_252_arg_marketcap_arg_equity(arg_marketcap, arg_equity): return _sd_ratio(arg_marketcap, arg_equity).rolling(252).mean()
def f19_share_and_dilution_snapshot_netinc_to_revenue_252_arg_netinc_arg_revenue(arg_netinc, arg_revenue): return _sd_ratio(arg_netinc, arg_revenue).rolling(252).mean()
def f19_share_and_dilution_snapshot_shareswa_to_revenue_252_arg_shareswa_arg_revenue(arg_shareswa, arg_revenue): return _sd_ratio(arg_shareswa, arg_revenue).rolling(252).mean()
def f19_share_and_dilution_snapshot_shareswa_to_equity_252_arg_shareswa_arg_equity(arg_shareswa, arg_equity): return _sd_ratio(arg_shareswa, arg_equity).rolling(252).mean()
def f19_share_and_dilution_snapshot_shareswa_dist_max_252_arg_shareswa(arg_shareswa): return arg_shareswa / (arg_shareswa.rolling(252).max() + 1e-8)
def f19_share_and_dilution_snapshot_shareswa_dist_min_252_arg_shareswa(arg_shareswa): return arg_shareswa / (arg_shareswa.rolling(252).min() + 1e-8)
def f19_share_and_dilution_snapshot_sharesbas_dist_max_252_arg_sharesbas(arg_sharesbas): return arg_sharesbas / (arg_sharesbas.rolling(252).max() + 1e-8)
def f19_share_and_dilution_snapshot_sharesbas_dist_min_252_arg_sharesbas(arg_sharesbas): return arg_sharesbas / (arg_sharesbas.rolling(252).min() + 1e-8)
def f19_share_and_dilution_snapshot_shareswa_growth_accel_252_arg_shareswa(arg_shareswa): return arg_shareswa.pct_change(252).diff(252)
def f19_share_and_dilution_snapshot_sharesbas_growth_accel_252_arg_sharesbas(arg_sharesbas): return arg_sharesbas.pct_change(252).diff(252)

_current_module = sys.modules[__name__]
f19_share_and_dilution_snapshot_BASE_REGISTRY_001_075 = {
    name: {"inputs": list(inspect.signature(obj).parameters.keys()), "func": obj}
    for name, obj in inspect.getmembers(_current_module, inspect.isfunction)
    if name.startswith("f19_share_and_dilution_snapshot_")
}

if __name__ == "__main__":
    # Synthetic test
    data = {
        'arg_shareswa': pd.Series(np.linspace(100, 110, 5000) + np.random.randn(5000)),
        'arg_sharesbas': pd.Series(np.linspace(90, 95, 5000) + np.random.randn(5000)),
        'arg_marketcap': pd.Series(np.linspace(1000, 1200, 5000) + np.random.randn(5000)),
        'arg_equity': pd.Series(np.linspace(500, 600, 5000) + np.random.randn(5000)),
        'arg_revenue': pd.Series(np.linspace(200, 250, 5000) + np.random.randn(5000)),
        'arg_netinc': pd.Series(np.linspace(20, 30, 5000) + np.random.randn(5000)),
    }
    df = pd.DataFrame(data)
    for name, info in f19_share_and_dilution_snapshot_BASE_REGISTRY_001_075.items():
        inputs = [df[inp] for inp in info['inputs']]
        q = info['func'](*inputs)
        assert len(q) > 0, f"{name} failed length check"
        assert q.nunique() > 2, f"{name} failed nunique check: {q.nunique()}"
        assert q.std() > 0, f"{name} failed std check: {q.std()}"
    print(f"All {len(f19_share_and_dilution_snapshot_BASE_REGISTRY_001_075)} features in f19_share_and_dilution_snapshot_BASE_REGISTRY_001_075 passed assertions.")
