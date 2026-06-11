import pandas as pd
import numpy as np

def _ea_ratio(num, den):
    return num / den.replace(0, np.nan)

def _ea_accel(s, w1, w2):
    return s.pct_change(w1).pct_change(w2)

def _ea_jerk(s, w1, w2):
    return s.diff(w1).diff(w2)

def _ea_z(s, w):
    return (s - s.rolling(w, min_periods=min(w, 10)).mean()) / s.rolling(w, min_periods=min(w, 10)).std().replace(0, np.nan)

# F33 Efficiency Acceleration - Jerk v001 to v150

def f33_efficiency_acceleration_asset_turn_accel_5d_jerk_v001_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_10d_jerk_v002_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 10, 21)
    res = _ea_jerk(base, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_21d_jerk_v003_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_5d_jerk_v004_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_21d_jerk_v005_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_5d_jerk_v006_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_21d_jerk_v007_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_5d_jerk_v008_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_21d_jerk_v009_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_5d_jerk_v010_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_21d_jerk_v011_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_5d_jerk_v012_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_21d_jerk_v013_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_5d_jerk_v014_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_21d_jerk_v015_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_z_5d_jerk_v016_signal(revenue, assets) -> pd.Series:
    """Jerk of Z-score of Asset Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, assets), 5, 21), 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_z_21d_jerk_v017_signal(revenue, assets) -> pd.Series:
    """Jerk of Z-score of Asset Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, assets), 21, 63), 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_z_5d_jerk_v018_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Z-score of Working Capital Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, workingcapital), 5, 21), 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_z_21d_jerk_v019_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Z-score of Working Capital Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, workingcapital), 21, 63), 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_z_5d_jerk_v020_signal(opinc, assets) -> pd.Series:
    """Jerk of Z-score of Operating Efficiency Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(opinc, assets), 5, 21), 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_z_21d_jerk_v021_signal(opinc, assets) -> pd.Series:
    """Jerk of Z-score of Operating Efficiency Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(opinc, assets), 21, 63), 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_z_5d_jerk_v022_signal(revenue, inventory) -> pd.Series:
    """Jerk of Z-score of Inventory Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, inventory), 5, 21), 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_z_21d_jerk_v023_signal(revenue, inventory) -> pd.Series:
    """Jerk of Z-score of Inventory Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, inventory), 21, 63), 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_z_5d_jerk_v024_signal(revenue, receivables) -> pd.Series:
    """Jerk of Z-score of Receivables Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, receivables), 5, 21), 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_z_21d_jerk_v025_signal(revenue, receivables) -> pd.Series:
    """Jerk of Z-score of Receivables Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, receivables), 21, 63), 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_z_5d_jerk_v026_signal(cogs, payables) -> pd.Series:
    """Jerk of Z-score of Payables Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(cogs, payables), 5, 21), 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_z_21d_jerk_v027_signal(cogs, payables) -> pd.Series:
    """Jerk of Z-score of Payables Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(cogs, payables), 21, 63), 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_z_5d_jerk_v028_signal(revenue, capex) -> pd.Series:
    """Jerk of Z-score of CAPEX Efficiency Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, capex), 5, 21), 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_z_21d_jerk_v029_signal(revenue, capex) -> pd.Series:
    """Jerk of Z-score of CAPEX Efficiency Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, capex), 21, 63), 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_equity_turn_accel_5d_jerk_v030_signal(revenue, equity) -> pd.Series:
    """Jerk of Equity Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, equity), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_equity_turn_accel_21d_jerk_v031_signal(revenue, equity) -> pd.Series:
    """Jerk of Equity Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, equity), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_liab_turn_accel_5d_jerk_v032_signal(revenue, liabilities) -> pd.Series:
    """Jerk of Liabilities Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, liabilities), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_liab_turn_accel_21d_jerk_v033_signal(revenue, liabilities) -> pd.Series:
    """Jerk of Liabilities Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, liabilities), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_emp_turn_accel_5d_jerk_v034_signal(revenue, employees) -> pd.Series:
    """Jerk of Employee Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, employees), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_emp_turn_accel_21d_jerk_v035_signal(revenue, employees) -> pd.Series:
    """Jerk of Employee Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, employees), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_5d_jerk_v036_signal(opinc, revenue) -> pd.Series:
    """Jerk of Operating Margin Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_21d_jerk_v037_signal(opinc, revenue) -> pd.Series:
    """Jerk of Operating Margin Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_5d_jerk_v038_signal(revenue, cogs) -> pd.Series:
    """Jerk of Gross Margin Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_21d_jerk_v039_signal(revenue, cogs) -> pd.Series:
    """Jerk of Gross Margin Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_5d_jerk_v040_signal(inventory, cogs) -> pd.Series:
    """Jerk of DSI Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_21d_jerk_v041_signal(inventory, cogs) -> pd.Series:
    """Jerk of DSI Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_5d_jerk_v042_signal(receivables, revenue) -> pd.Series:
    """Jerk of DSO Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_21d_jerk_v043_signal(receivables, revenue) -> pd.Series:
    """Jerk of DSO Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_5d_jerk_v044_signal(payables, cogs) -> pd.Series:
    """Jerk of DPO Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(payables, cogs), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_21d_jerk_v045_signal(payables, cogs) -> pd.Series:
    """Jerk of DPO Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(payables, cogs), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_5d_jerk_v046_signal(assets, equity) -> pd.Series:
    """Jerk of Leverage Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(assets, equity), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_21d_jerk_v047_signal(assets, equity) -> pd.Series:
    """Jerk of Leverage Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(assets, equity), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_5d_jerk_v048_signal(revenue, assets, liabilities) -> pd.Series:
    """Jerk of Net Asset Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_21d_jerk_v049_signal(revenue, assets, liabilities) -> pd.Series:
    """Jerk of Net Asset Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_5d_jerk_v050_signal(capex, assets) -> pd.Series:
    """Jerk of CAPEX Intensity Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(capex, assets), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_21d_jerk_v051_signal(capex, assets) -> pd.Series:
    """Jerk of CAPEX Intensity Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(capex, assets), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_5d_jerk_v052_signal(revenue, employees) -> pd.Series:
    """Jerk of Revenue per Employee Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, employees), 5, 21)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_21d_jerk_v053_signal(revenue, employees) -> pd.Series:
    """Jerk of Revenue per Employee Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, employees), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_126d_jerk_v054_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 63, 126)
    res = _ea_jerk(base, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_126d_jerk_v055_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 63, 126)
    res = _ea_jerk(base, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_126d_jerk_v056_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 63, 126)
    res = _ea_jerk(base, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_126d_jerk_v057_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 63, 126)
    res = _ea_jerk(base, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_126d_jerk_v058_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 63, 126)
    res = _ea_jerk(base, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_126d_jerk_v059_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 63, 126)
    res = _ea_jerk(base, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_126d_jerk_v060_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 63, 126)
    res = _ea_jerk(base, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_3d_jerk_v061_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 3, 10)
    res = _ea_jerk(base, 3, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_3d_jerk_v062_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 3, 10)
    res = _ea_jerk(base, 3, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_3d_jerk_v063_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 3, 10)
    res = _ea_jerk(base, 3, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_3d_jerk_v064_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 3, 10)
    res = _ea_jerk(base, 3, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_3d_jerk_v065_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 3, 10)
    res = _ea_jerk(base, 3, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_3d_jerk_v066_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 3, 10)
    res = _ea_jerk(base, 3, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_3d_jerk_v067_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 3, 10)
    res = _ea_jerk(base, 3, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_10d_jerk_v068_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 5, 10)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_10d_jerk_v069_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 5, 10)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_10d_jerk_v070_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 5, 10)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_10d_jerk_v071_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 5, 10)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_10d_jerk_v072_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 5, 10)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_10d_jerk_v073_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 5, 10)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_10d_jerk_v074_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 5, 10)
    res = _ea_jerk(base, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_63d_jerk_v075_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_63d_jerk_v076_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_63d_jerk_v077_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_63d_jerk_v078_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_63d_jerk_v079_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_63d_jerk_v080_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_63d_jerk_v081_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 21, 63)
    res = _ea_jerk(base, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_252d_jerk_v082_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 126, 252)
    res = _ea_jerk(base, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_252d_jerk_v083_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 126, 252)
    res = _ea_jerk(base, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_252d_jerk_v084_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 126, 252)
    res = _ea_jerk(base, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_252d_jerk_v085_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 126, 252)
    res = _ea_jerk(base, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_252d_jerk_v086_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 126, 252)
    res = _ea_jerk(base, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_252d_jerk_v087_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 126, 252)
    res = _ea_jerk(base, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_252d_jerk_v088_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 126, 252)
    res = _ea_jerk(base, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v089_jerk_v089_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, assets), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v090_jerk_v090_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v091_jerk_v091_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration variation."""
    base = _ea_accel(_ea_ratio(opinc, assets), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v092_jerk_v092_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v093_jerk_v093_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v094_jerk_v094_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(cogs, payables), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v095_jerk_v095_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, capex), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v096_jerk_v096_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, assets), 10, 63)
    res = _ea_jerk(base, 5, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v097_jerk_v097_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 10, 63)
    res = _ea_jerk(base, 5, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v098_jerk_v098_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(opinc, assets), 10, 63)
    res = _ea_jerk(base, 5, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v099_jerk_v099_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 10, 63)
    res = _ea_jerk(base, 5, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v100_jerk_v100_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 10, 63)
    res = _ea_jerk(base, 5, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v101_jerk_v101_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(cogs, payables), 10, 63)
    res = _ea_jerk(base, 5, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v102_jerk_v102_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, capex), 10, 63)
    res = _ea_jerk(base, 5, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v103_jerk_v103_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, assets), 21, 126)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v104_jerk_v104_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 21, 126)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v105_jerk_v105_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(opinc, assets), 21, 126)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v106_jerk_v106_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 21, 126)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v107_jerk_v107_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 21, 126)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v108_jerk_v108_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(cogs, payables), 21, 126)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v109_jerk_v109_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, capex), 21, 126)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_v110_jerk_v110_signal(opinc, revenue) -> pd.Series:
    """Jerk of Operating Margin Acceleration variation."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_v111_jerk_v111_signal(revenue, cogs) -> pd.Series:
    """Jerk of Gross Margin Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_v112_jerk_v112_signal(inventory, cogs) -> pd.Series:
    """Jerk of DSI Acceleration variation."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_v113_jerk_v113_signal(receivables, revenue) -> pd.Series:
    """Jerk of DSO Acceleration variation."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_v114_jerk_v114_signal(payables, cogs) -> pd.Series:
    """Jerk of DPO Acceleration variation."""
    base = _ea_accel(_ea_ratio(payables, cogs), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_v115_jerk_v115_signal(assets, equity) -> pd.Series:
    """Jerk of Leverage Acceleration variation."""
    base = _ea_accel(_ea_ratio(assets, equity), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_v116_jerk_v116_signal(revenue, assets, liabilities) -> pd.Series:
    """Jerk of Net Asset Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_v117_jerk_v117_signal(capex, assets) -> pd.Series:
    """Jerk of CAPEX Intensity Acceleration variation."""
    base = _ea_accel(_ea_ratio(capex, assets), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_v118_jerk_v118_signal(revenue, employees) -> pd.Series:
    """Jerk of Revenue per Employee Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, employees), 5, 63)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v119_jerk_v119_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, assets), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v120_jerk_v120_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v121_jerk_v121_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(opinc, assets), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v122_jerk_v122_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v123_jerk_v123_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v124_jerk_v124_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(cogs, payables), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v125_jerk_v125_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, capex), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_v126_jerk_v126_signal(opinc, revenue) -> pd.Series:
    """Jerk of Operating Margin Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_v127_jerk_v127_signal(revenue, cogs) -> pd.Series:
    """Jerk of Gross Margin Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_v128_jerk_v128_signal(inventory, cogs) -> pd.Series:
    """Jerk of DSI Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_v129_jerk_v129_signal(receivables, revenue) -> pd.Series:
    """Jerk of DSO Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_v130_jerk_v130_signal(payables, cogs) -> pd.Series:
    """Jerk of DPO Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(payables, cogs), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_v131_jerk_v131_signal(assets, equity) -> pd.Series:
    """Jerk of Leverage Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(assets, equity), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_v132_jerk_v132_signal(revenue, assets, liabilities) -> pd.Series:
    """Jerk of Net Asset Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_v133_jerk_v133_signal(capex, assets) -> pd.Series:
    """Jerk of CAPEX Intensity Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(capex, assets), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_v134_jerk_v134_signal(revenue, employees) -> pd.Series:
    """Jerk of Revenue per Employee Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, employees), 21, 252)
    res = _ea_jerk(base, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v135_jerk_v135_signal(revenue, assets) -> pd.Series:
    """Jerk of Asset Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, assets), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v136_jerk_v136_signal(revenue, workingcapital) -> pd.Series:
    """Jerk of Working Capital Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v137_jerk_v137_signal(opinc, assets) -> pd.Series:
    """Jerk of Operating Efficiency Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(opinc, assets), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v138_jerk_v138_signal(revenue, inventory) -> pd.Series:
    """Jerk of Inventory Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v139_jerk_v139_signal(revenue, receivables) -> pd.Series:
    """Jerk of Receivables Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v140_jerk_v140_signal(cogs, payables) -> pd.Series:
    """Jerk of Payables Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(cogs, payables), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v141_jerk_v141_signal(revenue, capex) -> pd.Series:
    """Jerk of CAPEX Efficiency Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, capex), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_v142_jerk_v142_signal(opinc, revenue) -> pd.Series:
    """Jerk of Operating Margin Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_v143_jerk_v143_signal(revenue, cogs) -> pd.Series:
    """Jerk of Gross Margin Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_v144_jerk_v144_signal(inventory, cogs) -> pd.Series:
    """Jerk of DSI Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_v145_jerk_v145_signal(receivables, revenue) -> pd.Series:
    """Jerk of DSO Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_v146_jerk_v146_signal(payables, cogs) -> pd.Series:
    """Jerk of DPO Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(payables, cogs), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_v147_jerk_v147_signal(assets, equity) -> pd.Series:
    """Jerk of Leverage Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(assets, equity), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_v148_jerk_v148_signal(revenue, assets, liabilities) -> pd.Series:
    """Jerk of Net Asset Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_v149_jerk_v149_signal(capex, assets) -> pd.Series:
    """Jerk of CAPEX Intensity Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(capex, assets), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_v150_jerk_v150_signal(revenue, employees) -> pd.Series:
    """Jerk of Revenue per Employee Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, employees), 10, 126)
    res = _ea_jerk(base, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1000
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum(),
        "assets": np.random.normal(5000, 500, n).cumsum(),
        "workingcapital": np.random.normal(100, 20, n).cumsum(),
        "opinc": np.random.normal(100, 20, n).cumsum(),
        "inventory": np.random.normal(200, 40, n).cumsum(),
        "receivables": np.random.normal(150, 30, n).cumsum(),
        "payables": np.random.normal(120, 25, n).cumsum(),
        "capex": np.random.normal(50, 10, n).cumsum(),
        "equity": np.random.normal(3000, 300, n).cumsum(),
        "liabilities": np.random.normal(2000, 200, n).cumsum(),
        "employees": np.random.normal(100, 10, n).cumsum() + 100,
        "cogs": np.random.normal(700, 70, n).cumsum(),
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f33_"))]
    
    print(f"Testing {len(funcs)} functions...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        # Test non-triviality
        q = y1.dropna()
        if len(q) > 0:
            assert q.nunique() > 10, f"Function {func.__name__} has too few unique values"
        
    print("All tests passed!")
