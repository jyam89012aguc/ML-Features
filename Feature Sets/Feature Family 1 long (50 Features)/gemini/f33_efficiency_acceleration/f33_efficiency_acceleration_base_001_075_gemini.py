import pandas as pd
import numpy as np

def _ea_ratio(num, den):
    return num / den.replace(0, np.nan)

def _ea_accel(s, w1, w2):
    return s.pct_change(w1).pct_change(w2)

def _ea_z(s, w):
    return (s - s.rolling(w, min_periods=min(w, 10)).mean()) / s.rolling(w, min_periods=min(w, 10)).std().replace(0, np.nan)

# F33 Efficiency Acceleration - Base v001 to v075

def f33_efficiency_acceleration_asset_turn_accel_5d_21d_base_v001_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_10d_21d_base_v002_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over 10d and 21d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 10, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_21d_63d_base_v003_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_5d_21d_base_v004_signal(revenue, workingcapital) -> pd.Series:
    """Acceleration of Working Capital Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, workingcapital)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_21d_63d_base_v005_signal(revenue, workingcapital) -> pd.Series:
    """Acceleration of Working Capital Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, workingcapital)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_5d_21d_base_v006_signal(opinc, assets) -> pd.Series:
    """Acceleration of Operating Efficiency (OpInc/Assets) over 5d and 21d."""
    ratio = _ea_ratio(opinc, assets)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_21d_63d_base_v007_signal(opinc, assets) -> pd.Series:
    """Acceleration of Operating Efficiency (OpInc/Assets) over 21d and 63d."""
    ratio = _ea_ratio(opinc, assets)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_5d_21d_base_v008_signal(revenue, inventory) -> pd.Series:
    """Acceleration of Inventory Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, inventory)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_21d_63d_base_v009_signal(revenue, inventory) -> pd.Series:
    """Acceleration of Inventory Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, inventory)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_5d_21d_base_v010_signal(revenue, receivables) -> pd.Series:
    """Acceleration of Receivables Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, receivables)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_21d_63d_base_v011_signal(revenue, receivables) -> pd.Series:
    """Acceleration of Receivables Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, receivables)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_5d_21d_base_v012_signal(cogs, payables) -> pd.Series:
    """Acceleration of Payables Turnover over 5d and 21d."""
    ratio = _ea_ratio(cogs, payables)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_21d_63d_base_v013_signal(cogs, payables) -> pd.Series:
    """Acceleration of Payables Turnover over 21d and 63d."""
    ratio = _ea_ratio(cogs, payables)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_5d_21d_base_v014_signal(revenue, capex) -> pd.Series:
    """Acceleration of CAPEX Efficiency over 5d and 21d."""
    ratio = _ea_ratio(revenue, capex)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_21d_63d_base_v015_signal(revenue, capex) -> pd.Series:
    """Acceleration of CAPEX Efficiency over 21d and 63d."""
    ratio = _ea_ratio(revenue, capex)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_z_5d_21d_base_v016_signal(revenue, assets) -> pd.Series:
    """Z-score of Acceleration of Asset Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, assets)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_z_21d_63d_base_v017_signal(revenue, assets) -> pd.Series:
    """Z-score of Acceleration of Asset Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, assets)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_z_5d_21d_base_v018_signal(revenue, workingcapital) -> pd.Series:
    """Z-score of Acceleration of Working Capital Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, workingcapital)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_z_21d_63d_base_v019_signal(revenue, workingcapital) -> pd.Series:
    """Z-score of Acceleration of Working Capital Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, workingcapital)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_z_5d_21d_base_v020_signal(opinc, assets) -> pd.Series:
    """Z-score of Acceleration of Operating Efficiency over 5d and 21d."""
    ratio = _ea_ratio(opinc, assets)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_z_21d_63d_base_v021_signal(opinc, assets) -> pd.Series:
    """Z-score of Acceleration of Operating Efficiency over 21d and 63d."""
    ratio = _ea_ratio(opinc, assets)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_z_5d_21d_base_v022_signal(revenue, inventory) -> pd.Series:
    """Z-score of Acceleration of Inventory Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, inventory)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_z_21d_63d_base_v023_signal(revenue, inventory) -> pd.Series:
    """Z-score of Acceleration of Inventory Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, inventory)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_z_5d_21d_base_v024_signal(revenue, receivables) -> pd.Series:
    """Z-score of Acceleration of Receivables Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, receivables)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_z_21d_63d_base_v025_signal(revenue, receivables) -> pd.Series:
    """Z-score of Acceleration of Receivables Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, receivables)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_z_5d_21d_base_v026_signal(cogs, payables) -> pd.Series:
    """Z-score of Acceleration of Payables Turnover over 5d and 21d."""
    ratio = _ea_ratio(cogs, payables)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_z_21d_63d_base_v027_signal(cogs, payables) -> pd.Series:
    """Z-score of Acceleration of Payables Turnover over 21d and 63d."""
    ratio = _ea_ratio(cogs, payables)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_z_5d_21d_base_v028_signal(revenue, capex) -> pd.Series:
    """Z-score of Acceleration of CAPEX Efficiency over 5d and 21d."""
    ratio = _ea_ratio(revenue, capex)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_z_21d_63d_base_v029_signal(revenue, capex) -> pd.Series:
    """Z-score of Acceleration of CAPEX Efficiency over 21d and 63d."""
    ratio = _ea_ratio(revenue, capex)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_equity_turn_accel_5d_21d_base_v030_signal(revenue, equity) -> pd.Series:
    """Acceleration of Equity Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, equity)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_equity_turn_accel_21d_63d_base_v031_signal(revenue, equity) -> pd.Series:
    """Acceleration of Equity Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, equity)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_liab_turn_accel_5d_21d_base_v032_signal(revenue, liabilities) -> pd.Series:
    """Acceleration of Liabilities Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, liabilities)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_liab_turn_accel_21d_63d_base_v033_signal(revenue, liabilities) -> pd.Series:
    """Acceleration of Liabilities Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, liabilities)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_emp_turn_accel_5d_21d_base_v034_signal(revenue, employees) -> pd.Series:
    """Acceleration of Employee Turnover (Rev/Emp) over 5d and 21d."""
    ratio = _ea_ratio(revenue, employees)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_emp_turn_accel_21d_63d_base_v035_signal(revenue, employees) -> pd.Series:
    """Acceleration of Employee Turnover (Rev/Emp) over 21d and 63d."""
    ratio = _ea_ratio(revenue, employees)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_126d_252d_base_v036_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over long windows 126d and 252d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_126d_252d_base_v037_signal(revenue, workingcapital) -> pd.Series:
    """Acceleration of Working Capital Turnover over long windows 126d and 252d."""
    ratio = _ea_ratio(revenue, workingcapital)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_126d_252d_base_v038_signal(opinc, assets) -> pd.Series:
    """Acceleration of Operating Efficiency over long windows 126d and 252d."""
    ratio = _ea_ratio(opinc, assets)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_126d_252d_base_v039_signal(revenue, inventory) -> pd.Series:
    """Acceleration of Inventory Turnover over long windows 126d and 252d."""
    ratio = _ea_ratio(revenue, inventory)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_126d_252d_base_v040_signal(revenue, receivables) -> pd.Series:
    """Acceleration of Receivables Turnover over long windows 126d and 252d."""
    ratio = _ea_ratio(revenue, receivables)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_126d_252d_base_v041_signal(cogs, payables) -> pd.Series:
    """Acceleration of Payables Turnover over long windows 126d and 252d."""
    ratio = _ea_ratio(cogs, payables)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_126d_252d_base_v042_signal(revenue, capex) -> pd.Series:
    """Acceleration of CAPEX Efficiency over long windows 126d and 252d."""
    ratio = _ea_ratio(revenue, capex)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_3d_10d_base_v043_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over short windows 3d and 10d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_3d_10d_base_v044_signal(revenue, workingcapital) -> pd.Series:
    """Acceleration of Working Capital Turnover over short windows 3d and 10d."""
    ratio = _ea_ratio(revenue, workingcapital)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_3d_10d_base_v045_signal(opinc, assets) -> pd.Series:
    """Acceleration of Operating Efficiency over short windows 3d and 10d."""
    ratio = _ea_ratio(opinc, assets)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_3d_10d_base_v046_signal(revenue, inventory) -> pd.Series:
    """Acceleration of Inventory Turnover over short windows 3d and 10d."""
    ratio = _ea_ratio(revenue, inventory)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_3d_10d_base_v047_signal(revenue, receivables) -> pd.Series:
    """Acceleration of Receivables Turnover over short windows 3d and 10d."""
    ratio = _ea_ratio(revenue, receivables)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_3d_10d_base_v048_signal(cogs, payables) -> pd.Series:
    """Acceleration of Payables Turnover over short windows 3d and 10d."""
    ratio = _ea_ratio(cogs, payables)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_3d_10d_base_v049_signal(revenue, capex) -> pd.Series:
    """Acceleration of CAPEX Efficiency over short windows 3d and 10d."""
    ratio = _ea_ratio(revenue, capex)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_10d_63d_base_v050_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over 10d and 63d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_10d_63d_base_v051_signal(revenue, workingcapital) -> pd.Series:
    """Acceleration of Working Capital Turnover over 10d and 63d."""
    ratio = _ea_ratio(revenue, workingcapital)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_10d_63d_base_v052_signal(opinc, assets) -> pd.Series:
    """Acceleration of Operating Efficiency over 10d and 63d."""
    ratio = _ea_ratio(opinc, assets)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_10d_63d_base_v053_signal(revenue, inventory) -> pd.Series:
    """Acceleration of Inventory Turnover over 10d and 63d."""
    ratio = _ea_ratio(revenue, inventory)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_10d_63d_base_v054_signal(revenue, receivables) -> pd.Series:
    """Acceleration of Receivables Turnover over 10d and 63d."""
    ratio = _ea_ratio(revenue, receivables)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_10d_63d_base_v055_signal(cogs, payables) -> pd.Series:
    """Acceleration of Payables Turnover over 10d and 63d."""
    ratio = _ea_ratio(cogs, payables)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_10d_63d_base_v056_signal(revenue, capex) -> pd.Series:
    """Acceleration of CAPEX Efficiency over 10d and 63d."""
    ratio = _ea_ratio(revenue, capex)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_63d_252d_base_v057_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over 63d and 252d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_63d_252d_base_v058_signal(revenue, workingcapital) -> pd.Series:
    """Acceleration of Working Capital Turnover over 63d and 252d."""
    ratio = _ea_ratio(revenue, workingcapital)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_63d_252d_base_v059_signal(opinc, assets) -> pd.Series:
    """Acceleration of Operating Efficiency over 63d and 252d."""
    ratio = _ea_ratio(opinc, assets)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_63d_252d_base_v060_signal(revenue, inventory) -> pd.Series:
    """Acceleration of Inventory Turnover over 63d and 252d."""
    ratio = _ea_ratio(revenue, inventory)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_63d_252d_base_v061_signal(revenue, receivables) -> pd.Series:
    """Acceleration of Receivables Turnover over 63d and 252d."""
    ratio = _ea_ratio(revenue, receivables)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_63d_252d_base_v062_signal(cogs, payables) -> pd.Series:
    """Acceleration of Payables Turnover over 63d and 252d."""
    ratio = _ea_ratio(cogs, payables)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_63d_252d_base_v063_signal(revenue, capex) -> pd.Series:
    """Acceleration of CAPEX Efficiency over 63d and 252d."""
    ratio = _ea_ratio(revenue, capex)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_5d_63d_base_v064_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over 5d and 63d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_5d_63d_base_v065_signal(revenue, workingcapital) -> pd.Series:
    """Acceleration of Working Capital Turnover over 5d and 63d."""
    ratio = _ea_ratio(revenue, workingcapital)
    res = _ea_accel(ratio, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_5d_63d_base_v066_signal(opinc, assets) -> pd.Series:
    """Acceleration of Operating Efficiency over 5d and 63d."""
    ratio = _ea_ratio(opinc, assets)
    res = _ea_accel(ratio, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_5d_63d_base_v067_signal(revenue, inventory) -> pd.Series:
    """Acceleration of Inventory Turnover over 5d and 63d."""
    ratio = _ea_ratio(revenue, inventory)
    res = _ea_accel(ratio, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_5d_63d_base_v068_signal(revenue, receivables) -> pd.Series:
    """Acceleration of Receivables Turnover over 5d and 63d."""
    ratio = _ea_ratio(revenue, receivables)
    res = _ea_accel(ratio, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_pay_turn_accel_5d_63d_base_v069_signal(cogs, payables) -> pd.Series:
    """Acceleration of Payables Turnover over 5d and 63d."""
    ratio = _ea_ratio(cogs, payables)
    res = _ea_accel(ratio, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_eff_accel_5d_63d_base_v070_signal(revenue, capex) -> pd.Series:
    """Acceleration of CAPEX Efficiency over 5d and 63d."""
    ratio = _ea_ratio(revenue, capex)
    res = _ea_accel(ratio, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_21d_126d_base_v071_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over 21d and 126d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 21, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_21d_126d_base_v072_signal(revenue, workingcapital) -> pd.Series:
    """Acceleration of Working Capital Turnover over 21d and 126d."""
    ratio = _ea_ratio(revenue, workingcapital)
    res = _ea_accel(ratio, 21, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_21d_126d_base_v073_signal(opinc, assets) -> pd.Series:
    """Acceleration of Operating Efficiency over 21d and 126d."""
    ratio = _ea_ratio(opinc, assets)
    res = _ea_accel(ratio, 21, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_inv_turn_accel_21d_126d_base_v074_signal(revenue, inventory) -> pd.Series:
    """Acceleration of Inventory Turnover over 21d and 126d."""
    ratio = _ea_ratio(revenue, inventory)
    res = _ea_accel(ratio, 21, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rec_turn_accel_21d_126d_base_v075_signal(revenue, receivables) -> pd.Series:
    """Acceleration of Receivables Turnover over 21d and 126d."""
    ratio = _ea_ratio(revenue, receivables)
    res = _ea_accel(ratio, 21, 126)
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
