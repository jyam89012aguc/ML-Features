import pandas as pd
import numpy as np

def _ea_ratio(num, den):
    return num / den.replace(0, np.nan)

def _ea_accel(s, w1, w2):
    return s.pct_change(w1).pct_change(w2)

def _ea_slope(s, w):
    return s.diff(w)

def _ea_z(s, w):
    return (s - s.rolling(w, min_periods=min(w, 10)).mean()) / s.rolling(w, min_periods=min(w, 10)).std().replace(0, np.nan)

# F33 Efficiency Acceleration - Slope v001 to v150

def f33_efficiency_acceleration_asset_turn_accel_5d_slope_v001_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_10d_slope_v002_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 10, 21)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_21d_slope_v003_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_5d_slope_v004_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_21d_slope_v005_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_5d_slope_v006_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_21d_slope_v007_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_5d_slope_v008_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_21d_slope_v009_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_5d_slope_v010_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_21d_slope_v011_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_5d_slope_v012_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_21d_slope_v013_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_5d_slope_v014_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_21d_slope_v015_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_z_5d_slope_v016_signal(revenue, assets) -> pd.Series:
    """Slope of Z-score of Asset Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, assets), 5, 21), 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_z_21d_slope_v017_signal(revenue, assets) -> pd.Series:
    """Slope of Z-score of Asset Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, assets), 21, 63), 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_z_5d_slope_v018_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Z-score of Working Capital Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, workingcapital), 5, 21), 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_z_21d_slope_v019_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Z-score of Working Capital Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, workingcapital), 21, 63), 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_z_5d_slope_v020_signal(opinc, assets) -> pd.Series:
    """Slope of Z-score of Operating Efficiency Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(opinc, assets), 5, 21), 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_z_21d_slope_v021_signal(opinc, assets) -> pd.Series:
    """Slope of Z-score of Operating Efficiency Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(opinc, assets), 21, 63), 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_z_5d_slope_v022_signal(revenue, inventory) -> pd.Series:
    """Slope of Z-score of Inventory Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, inventory), 5, 21), 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_z_21d_slope_v023_signal(revenue, inventory) -> pd.Series:
    """Slope of Z-score of Inventory Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, inventory), 21, 63), 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_z_5d_slope_v024_signal(revenue, receivables) -> pd.Series:
    """Slope of Z-score of Receivables Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, receivables), 5, 21), 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_z_21d_slope_v025_signal(revenue, receivables) -> pd.Series:
    """Slope of Z-score of Receivables Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, receivables), 21, 63), 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_z_5d_slope_v026_signal(cogs, payables) -> pd.Series:
    """Slope of Z-score of Payables Turnover Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(cogs, payables), 5, 21), 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_z_21d_slope_v027_signal(cogs, payables) -> pd.Series:
    """Slope of Z-score of Payables Turnover Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(cogs, payables), 21, 63), 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_z_5d_slope_v028_signal(revenue, capex) -> pd.Series:
    """Slope of Z-score of CAPEX Efficiency Acceleration over 5d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, capex), 5, 21), 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_z_21d_slope_v029_signal(revenue, capex) -> pd.Series:
    """Slope of Z-score of CAPEX Efficiency Acceleration over 21d."""
    base = _ea_z(_ea_accel(_ea_ratio(revenue, capex), 21, 63), 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_equity_turn_accel_5d_slope_v030_signal(revenue, equity) -> pd.Series:
    """Slope of Equity Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, equity), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_equity_turn_accel_21d_slope_v031_signal(revenue, equity) -> pd.Series:
    """Slope of Equity Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, equity), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_liab_turn_accel_5d_slope_v032_signal(revenue, liabilities) -> pd.Series:
    """Slope of Liabilities Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, liabilities), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_liab_turn_accel_21d_slope_v033_signal(revenue, liabilities) -> pd.Series:
    """Slope of Liabilities Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, liabilities), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_emp_turn_accel_5d_slope_v034_signal(revenue, employees) -> pd.Series:
    """Slope of Employee Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, employees), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_emp_turn_accel_21d_slope_v035_signal(revenue, employees) -> pd.Series:
    """Slope of Employee Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, employees), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_5d_slope_v036_signal(opinc, revenue) -> pd.Series:
    """Slope of Operating Margin Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_21d_slope_v037_signal(opinc, revenue) -> pd.Series:
    """Slope of Operating Margin Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_5d_slope_v038_signal(revenue, cogs) -> pd.Series:
    """Slope of Gross Margin Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_21d_slope_v039_signal(revenue, cogs) -> pd.Series:
    """Slope of Gross Margin Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_5d_slope_v040_signal(inventory, cogs) -> pd.Series:
    """Slope of DSI Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_21d_slope_v041_signal(inventory, cogs) -> pd.Series:
    """Slope of DSI Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_5d_slope_v042_signal(receivables, revenue) -> pd.Series:
    """Slope of DSO Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_21d_slope_v043_signal(receivables, revenue) -> pd.Series:
    """Slope of DSO Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_5d_slope_v044_signal(payables, cogs) -> pd.Series:
    """Slope of DPO Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(payables, cogs), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_21d_slope_v045_signal(payables, cogs) -> pd.Series:
    """Slope of DPO Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(payables, cogs), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_5d_slope_v046_signal(assets, equity) -> pd.Series:
    """Slope of Leverage Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(assets, equity), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_21d_slope_v047_signal(assets, equity) -> pd.Series:
    """Slope of Leverage Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(assets, equity), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_5d_slope_v048_signal(revenue, assets, liabilities) -> pd.Series:
    """Slope of Net Asset Turnover Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_21d_slope_v049_signal(revenue, assets, liabilities) -> pd.Series:
    """Slope of Net Asset Turnover Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_5d_slope_v050_signal(capex, assets) -> pd.Series:
    """Slope of CAPEX Intensity Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(capex, assets), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_21d_slope_v051_signal(capex, assets) -> pd.Series:
    """Slope of CAPEX Intensity Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(capex, assets), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_5d_slope_v052_signal(revenue, employees) -> pd.Series:
    """Slope of Revenue per Employee Acceleration over 5d."""
    base = _ea_accel(_ea_ratio(revenue, employees), 5, 21)
    res = _ea_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_21d_slope_v053_signal(revenue, employees) -> pd.Series:
    """Slope of Revenue per Employee Acceleration over 21d."""
    base = _ea_accel(_ea_ratio(revenue, employees), 21, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_126d_slope_v054_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 63, 126)
    res = _ea_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_126d_slope_v055_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 63, 126)
    res = _ea_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_126d_slope_v056_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 63, 126)
    res = _ea_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_126d_slope_v057_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 63, 126)
    res = _ea_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_126d_slope_v058_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 63, 126)
    res = _ea_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_126d_slope_v059_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 63, 126)
    res = _ea_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_126d_slope_v060_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration over 126d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 63, 126)
    res = _ea_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_3d_slope_v061_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 3, 10)
    res = _ea_slope(base, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_3d_slope_v062_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 3, 10)
    res = _ea_slope(base, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_3d_slope_v063_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 3, 10)
    res = _ea_slope(base, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_3d_slope_v064_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 3, 10)
    res = _ea_slope(base, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_3d_slope_v065_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 3, 10)
    res = _ea_slope(base, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_3d_slope_v066_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 3, 10)
    res = _ea_slope(base, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_3d_slope_v067_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration over 3d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 3, 10)
    res = _ea_slope(base, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_10d_slope_v068_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 5, 10)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_10d_slope_v069_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 5, 10)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_10d_slope_v070_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 5, 10)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_10d_slope_v071_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 5, 10)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_10d_slope_v072_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 5, 10)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_10d_slope_v073_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 5, 10)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_10d_slope_v074_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration over 10d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 5, 10)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_63d_slope_v075_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 21, 63)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_63d_slope_v076_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 21, 63)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_63d_slope_v077_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 21, 63)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_63d_slope_v078_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 21, 63)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_63d_slope_v079_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 21, 63)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_63d_slope_v080_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 21, 63)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_63d_slope_v081_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration over 63d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 21, 63)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_252d_slope_v082_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, assets), 126, 252)
    res = _ea_slope(base, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_252d_slope_v083_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 126, 252)
    res = _ea_slope(base, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_252d_slope_v084_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(opinc, assets), 126, 252)
    res = _ea_slope(base, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_252d_slope_v085_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 126, 252)
    res = _ea_slope(base, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_252d_slope_v086_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 126, 252)
    res = _ea_slope(base, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_252d_slope_v087_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(cogs, payables), 126, 252)
    res = _ea_slope(base, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_252d_slope_v088_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration over 252d."""
    base = _ea_accel(_ea_ratio(revenue, capex), 126, 252)
    res = _ea_slope(base, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v089_slope_v089_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, assets), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v090_slope_v090_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v091_slope_v091_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration variation."""
    base = _ea_accel(_ea_ratio(opinc, assets), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v092_slope_v092_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v093_slope_v093_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v094_slope_v094_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(cogs, payables), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v095_slope_v095_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, capex), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v096_slope_v096_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, assets), 10, 63)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v097_slope_v097_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 10, 63)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v098_slope_v098_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(opinc, assets), 10, 63)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v099_slope_v099_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 10, 63)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v100_slope_v100_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 10, 63)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v101_slope_v101_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(cogs, payables), 10, 63)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v102_slope_v102_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, capex), 10, 63)
    res = _ea_slope(base, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v103_slope_v103_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, assets), 21, 126)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v104_slope_v104_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 21, 126)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v105_slope_v105_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(opinc, assets), 21, 126)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v106_slope_v106_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 21, 126)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v107_slope_v107_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 21, 126)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v108_slope_v108_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(cogs, payables), 21, 126)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v109_slope_v109_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, capex), 21, 126)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_v110_slope_v110_signal(opinc, revenue) -> pd.Series:
    """Slope of Operating Margin Acceleration variation."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_v111_slope_v111_signal(revenue, cogs) -> pd.Series:
    """Slope of Gross Margin Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_v112_slope_v112_signal(inventory, cogs) -> pd.Series:
    """Slope of DSI Acceleration variation."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_v113_slope_v113_signal(receivables, revenue) -> pd.Series:
    """Slope of DSO Acceleration variation."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_v114_slope_v114_signal(payables, cogs) -> pd.Series:
    """Slope of DPO Acceleration variation."""
    base = _ea_accel(_ea_ratio(payables, cogs), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_v115_slope_v115_signal(assets, equity) -> pd.Series:
    """Slope of Leverage Acceleration variation."""
    base = _ea_accel(_ea_ratio(assets, equity), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_v116_slope_v116_signal(revenue, assets, liabilities) -> pd.Series:
    """Slope of Net Asset Turnover Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_v117_slope_v117_signal(capex, assets) -> pd.Series:
    """Slope of CAPEX Intensity Acceleration variation."""
    base = _ea_accel(_ea_ratio(capex, assets), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_v118_slope_v118_signal(revenue, employees) -> pd.Series:
    """Slope of Revenue per Employee Acceleration variation."""
    base = _ea_accel(_ea_ratio(revenue, employees), 5, 63)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v119_slope_v119_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, assets), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v120_slope_v120_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v121_slope_v121_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(opinc, assets), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v122_slope_v122_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v123_slope_v123_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v124_slope_v124_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(cogs, payables), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v125_slope_v125_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration variation 4."""
    base = _ea_accel(_ea_ratio(revenue, capex), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_v126_slope_v126_signal(opinc, revenue) -> pd.Series:
    """Slope of Operating Margin Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_v127_slope_v127_signal(revenue, cogs) -> pd.Series:
    """Slope of Gross Margin Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_v128_slope_v128_signal(inventory, cogs) -> pd.Series:
    """Slope of DSI Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_v129_slope_v129_signal(receivables, revenue) -> pd.Series:
    """Slope of DSO Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_v130_slope_v130_signal(payables, cogs) -> pd.Series:
    """Slope of DPO Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(payables, cogs), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_v131_slope_v131_signal(assets, equity) -> pd.Series:
    """Slope of Leverage Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(assets, equity), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_v132_slope_v132_signal(revenue, assets, liabilities) -> pd.Series:
    """Slope of Net Asset Turnover Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_v133_slope_v133_signal(capex, assets) -> pd.Series:
    """Slope of CAPEX Intensity Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(capex, assets), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_v134_slope_v134_signal(revenue, employees) -> pd.Series:
    """Slope of Revenue per Employee Acceleration variation 2."""
    base = _ea_accel(_ea_ratio(revenue, employees), 21, 252)
    res = _ea_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_v135_slope_v135_signal(revenue, assets) -> pd.Series:
    """Slope of Asset Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, assets), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_v136_slope_v136_signal(revenue, workingcapital) -> pd.Series:
    """Slope of Working Capital Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, workingcapital), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_v137_slope_v137_signal(opinc, assets) -> pd.Series:
    """Slope of Operating Efficiency Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(opinc, assets), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_v138_slope_v138_signal(revenue, inventory) -> pd.Series:
    """Slope of Inventory Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, inventory), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_v139_slope_v139_signal(revenue, receivables) -> pd.Series:
    """Slope of Receivables Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, receivables), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_v140_slope_v140_signal(cogs, payables) -> pd.Series:
    """Slope of Payables Turnover Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(cogs, payables), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_v141_slope_v141_signal(revenue, capex) -> pd.Series:
    """Slope of CAPEX Efficiency Acceleration variation 5."""
    base = _ea_accel(_ea_ratio(revenue, capex), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_v142_slope_v142_signal(opinc, revenue) -> pd.Series:
    """Slope of Operating Margin Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(opinc, revenue), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_v143_slope_v143_signal(revenue, cogs) -> pd.Series:
    """Slope of Gross Margin Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, cogs), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_v144_slope_v144_signal(inventory, cogs) -> pd.Series:
    """Slope of DSI Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(inventory, cogs), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_v145_slope_v145_signal(receivables, revenue) -> pd.Series:
    """Slope of DSO Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(receivables, revenue), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_v146_slope_v146_signal(payables, cogs) -> pd.Series:
    """Slope of DPO Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(payables, cogs), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_v147_slope_v147_signal(assets, equity) -> pd.Series:
    """Slope of Leverage Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(assets, equity), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_v148_slope_v148_signal(revenue, assets, liabilities) -> pd.Series:
    """Slope of Net Asset Turnover Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, assets - liabilities), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_v149_slope_v149_signal(capex, assets) -> pd.Series:
    """Slope of CAPEX Intensity Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(capex, assets), 10, 126)
    res = _ea_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_v150_slope_v150_signal(revenue, employees) -> pd.Series:
    """Slope of Revenue per Employee Acceleration variation 3."""
    base = _ea_accel(_ea_ratio(revenue, employees), 10, 126)
    res = _ea_slope(base, 21)
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
